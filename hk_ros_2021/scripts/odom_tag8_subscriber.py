#!/usr/bin/env python
import rospy
import math
import tf
import geometry_msgs.msg
import tf2_ros
from std_msgs.msg import String



def callback8():   
    #rospy.init_node('odom_tag8_subscriber_node')

    listener = tf.TransformListener()

    rate = rospy.Rate(1) #one message per second

    #listener.waitForTransform('/odom', '/tag_9', rospy.Time(), rospy.Duration(60))
    
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/odom', '/tag_8', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        print '[',trans[0]*(-1),',',trans[1]*(-1),']' 
					                		
 	
	x8 = str(trans[0]*(-1))            #Multiply with -1 to transform the given coordinates
	y8 = str(trans[1]*(-1))            #to match the odom frame orientation
	coordinates8 = x8 + ", " + y8
	#rate.sleep()
	return coordinates8
	
if __name__ == '__main__':
	callback8()
