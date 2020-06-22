#!/usr/bin/env python3
name = 'yfactor_with_v_by_spectrometer'

import sys
import rospy
import time
import std_msgs.msg
import numpy
import argparse
import datetime

sys.path.append("../../necst-core/scripts")

import controller
import core_controller

rospy.init_node(name)

logger = core_controller.logger()
sis = controller.sis()

status = rospy.Publisher('/'+name+'/status', std_msgs.msg.String, queue_size=1)

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'
print(file_name)


# set params.

initial_voltage = 0.  # mV
final_voltage   = 8. # mV
step            = 0.05 # mV
integ_time      = 0.5
roop = int((final_voltage - initial_voltage) / step)


logger.start(file_name)
sis.set_v(float(initial_voltage))

time.sleep(1)

input('READY HOT MEASUREMENT? PRESS ENTER!!')
status.publish("{0:4}".format("hot"))

for i in range(roop+1):
    v = initial_voltage + i*step
    sis.set_v(float(v))
    time.sleep(integ_time)

sis.set_v(float(initial_voltage))

input('READY COLD MEASUREMENT? PRESS ENTER!!')
status.publish("{0:4}".format("cold"))

for i in range(roop+1):
    v = initial_voltage + i*step
    sis.set_v(float(v))
    time.sleep(integ_time)
status.publish("{0:4}".format("hot"))
time.sleep(0.1)
logger.stop()

sis.set_v(0)

print('')
print('FINISH!!')
print('')
