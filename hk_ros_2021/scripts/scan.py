#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):

	print len(msg.ranges)

	#print msg.ranges(0)

rospy.init_node('scan_values')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
