#!/usr/bin/env python
import rospy
import math
import tf
import geometry_msgs.msg
import tf2_ros
import tf2_geometry_msgs
#include "std_msgs/Header.h"
#include "geometry_msgs/PoseWithCovariance.h

#from nav_msgs.msg import Odometry
#from tf.msg import tfMessage

#from apriltag_ros import ApriltagDetectionArray
#from geometry_msgs import PoseWithCovariance
#from AprilTagDetectionArray.msg import AprilTagDetection
#include <apriltags_ros/AprilTagDetectionArray.h>
from apriltag_ros.msg import AprilTagDetectionArray
from apriltag_ros.msg import AprilTagDetection
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped, Point





def callback(detectionarray):

    #pub = rospy.Subscriber('tag_detections', AprilTagDetection , chatter_callback)
    #rospy.init_node('odom_tag8',anonymous = True)
    #msg = rospy.wait_for_message("/tag_detections", Pose)
    #rospy.init_node('odom_tag3',anonymous = True)
    listener = tf.TransformListener()
    #rate = rospy.Rate(1) # 10hz

    rate = rospy.Rate(1) #one message per second
    frame_id = str(detectionarray.detections[0].id)
    tag_frame = "/tag_"+frame_id[1:2]        #Getting the number out of frame_id
    #print(tag_frame)
    #print(detectionarray.detections)
    print(Point.x)
    test = detectionarray.detections
    #listener.waitForTransform('/odom', tag, rospy.Time(), rospy.Duration(60))
    #print(geometry_msgs/PoseWithCovariance)
    #while not rospy.is_shutdown():
        #try:
    print(PoseWithCovarianceStamped.pose)
    (trans,rot) = listener.lookupTransform('/odom', PoseWithCovarianceStamped.pose, rospy.Time(0))
        #except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
    print trans        #continue

        #print '[',trans[0]*(-1),',',trans[1]*(-1),']'
        #frame_id = str(detectionarray.detections[0].id)
        #tag_frame = "/tag_"+frame_id[1:2]
    #x = str(trans[0]*(-1))            #Multiply with -1 to transform the given coordinates
    #y = str(trans[1]*(-1))            #to match the odom frame orientation
    #coordinates = (x + ", " + y)

        #rate.sleep()
    #print trans
    #return coordinates

#def listener():
   #try:
	   #rospy.init_node('odom_tag9',anonymous = True)

   #except rospy.ROSInterrupException:
      #rospy.loginfo("node terminated.")

if __name__ == '__main__':
    rospy.init_node('odom_tag9',anonymous = True)

    pub = rospy.Subscriber('/tag_detections', AprilTagDetectionArray , callback)
   #rate = rospy.Rate(1) # 10hz
    rospy.spin()

   #except rospy.ROSInterrupException:
      #rospy.loginfo("node terminated.")
#https://stackoverflow.com/questions/56054356/in-ros-how-to-transform-pose-from-kinect-frame-to-pr2s-base-link-frame
    #try:
    #rospy.init_node('odom_tag9',anonymous = True)

    #pub = rospy.Subscriber('/tag_detections', AprilTagDetectionArray , callback)
     #rate = rospy.Rate(1) # 10hz
    #rospy.spin()
    #except rospy.ROSInterruptException:
        #pass
