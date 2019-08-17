#!/usr/bin/env python3

name = 'sis_i_v_curve_direction'

import sys
import rospy
import time
import std_msgs.msg
import numpy
import argparse

sys.path.append("/home/exito/ros/src/necst-core/scripts")
sys.path.append("/home/exito/ros/src/necst-dsb_evaluation2019/scripts")

import dsb_evaluation2019_controller
import core_controller

rospy.init_node(name)

sis = dsb_evaluation2019_controller.sis()
logger = core_controller.logger()

parser = argparse.ArgumentParser(description = 'measure SIS I-V curve only')

parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()

file_name = '/home/exito/data/logger/sis-iv/%s'%(args.save_name)
print(file_name)
#logger.start(file_name)
sis_vgap = numpy.arange(-1.2, 1.2, 0.001)
sis.set_vgap(-1.2)
time.sleep(3)
logger.start(file_name)
for vgap in sis_vgap:
    sis.set_vgap(vgap)
    time.sleep(0.03)
    continue
logger.stop()
sis.set_vgap(0)
