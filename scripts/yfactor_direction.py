#!/usr/bin/env python3

name = 'measure_yfactor_direction'

import sys
import datetime
import rospy
import time
import std_msgs.msg
import argparse

sys.path.append("/home/exito/ros/src/necst-core/scripts")
sys.path.append("/home/exito/ros/src/necst-dsb_evaluation2019/scripts")

import controller
import core_controller
import dsb_evaluation2019_controller

rospy.init_node(name)

sis = dsb_evaluation2019_controller.sis()
#loatt = controller.loatt()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'measure Y-factor only')
parser.add_argument('save_name', type = str, help = 'set saving file name')
parser.add_argument('sis_v', type = float, help = 'set sis_v')
parser.add_argument('measure_time', type = float, help = 'set measure time')
args = parser.parse_args()

date = datetime.datetime.today().strftime('%Y%m%d')
input('READY HOT MEASUREMENT? PRESS ENTER!!')

file_name = '/home/exito/data/evaluation/' + date + '/yfactor/%s/hot'%(args.save_name)
sis.set_v(args.sis_v)
time.sleep(1)
logger.start(file_name)
time.sleep(args.measure_time)
logger.stop()

input('READY COLD MEASUREMENT? PRESS ENTER!!')

file_name = '/home/exito/data/evaluation/' + date + '/yfactor/%s/cold'%(args.save_name)
logger.start(file_name)
time.sleep(args.measure_time)
logger.stop()

