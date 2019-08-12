#!/usr/bin/env python3

name = 'measure_yfactor_search_sis_vol_direction'

import sys
import rospy
import time
import std_msgs.msg
import numpy as np
import argparse

sys.path.append("/home/exito/ros/src/necst-core/scripts")

import controller
import core_controller

rospy.init_node(name)

sis = controller.sis()
loatt = controller.loatt()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'search optical sis voltage value')

parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()

file_name = '/home/exito/data/logger/%s'%(args.save_name)
volp = np.linespace(-1, 0, 5)   #search optimal SIS voltage value
logger.start(file_name)
for vp in volp:             #measure y-factor
    sis.set_vp(vp)
    time.sleep(1)
    continue
sis.set_vgap(0)
logger.stop()
