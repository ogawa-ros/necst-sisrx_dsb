#!/usr/bin/env python3

name = 'sis_iv'

import sys
import datetime
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

<<<<<<< HEAD
date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'
=======
parser = argparse.ArgumentParser(description = 'measure SIS I-V curve only')

parser.add_argument('save_name', type = str, help = 'set saving file name')

args = parser.parse_args()

date = datetime.datetime.today().strftime('%Y%m%d')
file_name = '/home/exito/data/evaluation/' + date + '/sis_iv/%s'%(args.save_name)
>>>>>>> a1c25db8e57bd86a31ab7b9c75c07ee6fe8755e5
print(file_name)

sis_vgap = numpy.arange(-1.2, 1.2, 0.005)
sis.set_vgap(0.3)
time.sleep(3)
logger.start(file_name)
for vgap in sis_vgap:
    sis.set_vgap(vgap)
    time.sleep(0.2)
    continue
logger.stop()
sis.set_vgap(0)
