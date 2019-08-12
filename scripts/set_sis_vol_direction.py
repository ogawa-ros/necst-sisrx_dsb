#!/usr/bin/env python3

name = 'set_sis_vol_direction'

import rospy
import time
import std_msgs.msg
import argparse

import controller

rospy.init_node(name)

sis = controller.sis()

parser = argparse.ArgumentParser(description = 'set SIS voltage V')

parser.add_argument('v', type = float, help = 'set SIS voltage of V')

args = parser.parse_args()

sis.set_vp(args.v)
