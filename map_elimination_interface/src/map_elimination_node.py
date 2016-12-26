#!/usr/bin/env python
# -*-coding:Utf-8 -*

import rospy
import numpy as np
import algorithm.exploration as exp

from geometry_msgs.msg import Twist,PoseArray,PoseWithCovarianceStamped
from sensor_msgs.msg import LaserScan
from amcl.msg import PoseArrayPlus
from std_srvs.srv import Empty
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import String

class map_elimination_node:

    def __init__ (self):
        self.number_maps = 3
        self.particlecloud = PoseArray()
        self.AmclPose = PoseWithCovarianceStamped()

        self.current_maps = np.linspace(1, self.number_maps, self.number_maps)
        self.maps_value = np.zeros(self.number_maps)
        self.maps = []
        self.iteration = 0
	self.iterationnumber = 0


        self.node = rospy.init_node("map_elimination_node", anonymous=True)

        self.output = rospy.Publisher("/terminalmessage", String, queue_size=1,latch=True)
        rospy.Subscriber("/map", OccupancyGrid, self.maps_callback)
        rospy.Subscriber("/particlecloud", PoseArray, self.input_callback)

        rospy.wait_for_service('/global_localization')
        try:
            res_cloud = rospy.ServiceProxy('/global_localization', Empty)
            res_cloud()
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e



        rospy.spin()


    def input_callback (self, Data):
        self.iteration += 1
        self.particlecloud = Data.poses
        self.maps_value += exp.simple_exploration(self.maps, self.current_maps, self.particlecloud)
        print("--------------------------------------------------------------------------------")
        #for i in range(0, self.number_maps):
            #print "The current similarity value for", (i+1),"th map is:", self.maps_value[i]
        print "The", self.iteration,"th iteration."

        #for j in range(len(self.current_maps)):
            #if self.maps_value[j] < -10:
                #print "The",(j+1),"th map has been eliminated!"
                #self.current_maps = np.delete(self.current_maps, j)

        #if len(self.maps_value) == 1:
        if self.iteration + self.iterationnumber == 26:
	    self.iterationnumber += 2
            self.output.publish("There is only one map left!")
            print "There is only the 2nd map left!"
	    self.iteration = 1;

        if len(self.maps_value) == 0:
            print "Start the recovery program"
            exp.elimination_recovery



    def maps_callback (self, Data):
        self.maps = Data.data

if __name__ == '__main__':
	elimination = map_elimination_node()
