#!/usr/bin/env python3

name = 'alan_dispersion'

import sys
import datetime
import rospy
import time
from std_msgs.msg import Float64
import numpy
import argparse
import datetime

sys.path.append("../../necst-core/scripts")

import core_controller

rospy.init_node(name)

logger = core_controller.logger()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'

print(file_name)

logger.start(file_name)
#measure time
time.sleep(10000)

logger.stop()
