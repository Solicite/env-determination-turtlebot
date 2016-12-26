#!/usr/bin/env python
# -*-coding:Utf-8 -*

import glob,os
import map_emerger as me

if __name__ == "__main__":
    me.map_emerge("./", ".png")

    worldfile = open('./emergedmap.world','w')

    worldfile.write('include "turtlebot.inc"'+ '\n\n')
    worldfile.write('define floorplan model'+'\n')
    worldfile.write('('+'\n')
    worldfile.write('  color "gray30"'+'\n')
    worldfile.write('  boundry 1'+'\n')
    worldfile.write('  gui_nose 0'+'\n')
    worldfile.write('  gui_grid 0'+'\n')
    worldfile.write('  gui_outline 0'+'\n')
    worldfile.write('  gripper_return 0'+'\n')
    worldfile.write('  fiducial_return 0'+'\n')
    worldfile.write('  laser_return 1'+'\n'+')'+'\n\n')

    worldfile.write('resolution 0.02\ninterval_sim 100\n\n')

    worldfile.write('window\n(\n  size [ 600.0 700.0 ]\n  center [ 0.0 0.0 ]\n  rotate [ 0.0 0.0 ]\n  scale 60\n)\n\n')

    worldfile.write('floorplan\n(\n  name "emergedmap"\n  bitmap "../merged.png"\n  size [ 10.0 30.0 2.0 ]\n  pose [ 5.0 5.0 0.0 0.0 ]\n)\n\n')

    worldfile.write('turtlebot\n(\n  pose [ 1.0 1.0 0.0 0.0 ]\n  name "turtlebot"\n  color "black"\n)\n')
