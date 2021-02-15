#!/usr/bin/env python
import rospy
import math
import tf
import geometry_msgs.msg
import tf2_ros
#from nav_msgs.msg import Odometry
#from tf.msg import tfMessage
from std_msgs.msg import String
#from apriltag_ros import ApriltagDetectionArray






def callback(): 

    pub = rospy.Publisher('chatter', String, queue_size=20)  
    rospy.init_node('odom_tag9',anonymous = True)
    #msg = rospy.wait_for_message("/std_msgs.msg", String)
    listener = tf.TransformListener()
    rate = rospy.Rate(10) # 10hz
  
    #rate = rospy.Rate(1) #one message per second
    #a = msg.coordinates
    #print AprilTagDetectionArray

    #listener.waitForTransform('/odom', '/tag_9', rospy.Time(), rospy.Duration(60))
    
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/odom', '/tag_9' , rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        #print '[',trans[0]*(-1),',',trans[1]*(-1),']' 
				                		
 	
	x = str(trans[0]*(-1))            #Multiply with -1 to transform the given coordinates
	y = str(trans[1]*(-1))            #to match the odom frame orientation
	coordinates = (x + ", " + y) #% rospy.get_time()
        rospy.loginfo(coordinates)
        pub.publish(coordinates)
        rate.sleep()
	
if __name__ == '__main__':
        try:
           callback()
	except rospy.ROSInterruptException:
           pass
	
