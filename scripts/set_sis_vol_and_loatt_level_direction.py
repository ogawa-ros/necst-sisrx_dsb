#!/usr/bin/env python3

name = 'set_sis_vol_and_att_level_direction'

import rospy
import time
import std_msgs.msg
import argparse

import controller

rospy.init_node(name)

sis = controller.sis()
att = controller.loatt()

parser = argparse.ArgumentParser(description = 'set SIS voltage V and Lo Att. level')

parser.add_argument('v', type = float, help = 'set SIS voltage of V')
parser.add_argument('att', type = float, help = 'set Lo Att. level')

args = parser.parse_args()

sis.set_vp(args.v)
att.set_cur(args.att)
