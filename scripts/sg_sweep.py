#!/usr/bin/env python3

name = 'sg_sweep'

import sys
import datetime
import rospy
import time
from std_msgs.msg import Float64
import numpy
import argparse
import datetime

sys.path.append("../../necst-core/scripts")

import controller
import core_controller

rospy.init_node(name)

logger = core_controller.logger()

sg_freq = rospy.Publisher('/dev/e8257d/ip_192_168_100_37/freq_cmd',Float64,queue_size=1)
sg_power = rospy.Publisher('/dev/e8257d/ip_192_168_100_37/power_cmd',Float64,queue_size=1)

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'

print(file_name)

#set power
power = input("How much sg power?? [dBm] ")
sg_power.publish(power)
time.slepp(0.1)

#set freq&sweep
start_freq = 0 #GHz
end_freq = 20  #GHz
freq_width = 5E-3 #GHz


sg_freq.publish(start_freq)
time.sleep(0.1)

logger.start(file_name)
time.sleep(1)

for i in range(start_freq,end_freq+1E-8,freq_width):
    sg_freq.publish(i)
    time.sleep(0.1)
    continue

time.sleep(2)
logger.stop()




