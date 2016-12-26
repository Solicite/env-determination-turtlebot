#!/usr/bin/env python
# -*-coding:Utf-8 -*


#This function calculate the value function of each candidated map in every round

import rospy
import numpy as np

def simple_exploration(maps, current_maps, particlecloud):
    imediate_value, normalized_value = np.zeros(3), []

    for particle in particlecloud:
        if maps[ int( np.ceil( particle.position.x * 12000 + particle.position.y * 20 ) ) % 120000] == 100:
            imediate_value[int( np.ceil( particle.position.x * 12000 + particle.position.y * 20 ) ) % 120000 / 40000] -= 30
        else:
            imediate_value[int( np.ceil( particle.position.x * 12000 + particle.position.y * 20 ) ) % 120000 / 40000] += 1



    max_value = np.absolute(np.max(imediate_value))

    for value in imediate_value:
        normalized_value.append(value/max_value)

    return normalized_value
