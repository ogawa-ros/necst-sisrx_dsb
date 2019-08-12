#!/usr/bin/env python3

name = 'measure_yfactor_direction'

import sys
import rospy
import time
import std_msgs.msg
import argparse

sys.path.append("/home/exito/ros/src/necst-core/scripts")

import controller
import core_controller

rospy.init_node(name)

sis = controller.sis()
#loatt = controller.loatt()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'measure Y-factor only')
parser.add_argument('save_name', type = str, help = 'set saving file name')
parser.add_argument('sis_v', type = float, help = 'set sis_v')
parser.add_argument('measure_time', type = float, help = 'set measure time')
args = parser.parse_args()

input('READY HOT MEASUREMENT? PRESS ENTER!!')

file_name = '/home/exito/data/logger/yfactor/hot/%s'%(args.save_name)
logger.start(file_name)
sis.set_v(args.sis_v)
time.sleep(args.measure_time)
logger.stop()

input('READY COLD MEASUREMENT? PRESS ENTER!!')

file_name = '/home/exito/data/logger/yfactor/cold/%s'%(args.save_name)
logger.start(file_name)
sis.set_v(args.sis_v)
time.sleep(args.measure_time)
logger.stop()
