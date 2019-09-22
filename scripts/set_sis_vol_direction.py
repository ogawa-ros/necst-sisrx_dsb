#!/usr/bin/env python3

name = 'set_sis_vol_direction'

import rospy
import controller

rospy.init_node(name)
sis = controller.sis()

vol = input("How much Voltage?? [mV] ")

sis.set_vp(float(vol))
