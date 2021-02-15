#!/usr/bin/env python
import rospy # the ROS api for python. We need it to create a node,              # a subscriber and access other ROS-specific program control
from nav_msgs.msg import Odometry # Python message class for Odometry
import geometry_msgs.msg


rospy.init_node("extra_message_node")
msg = rospy.wait_for_message("/odom", Odometry)
print "Full message: \n"
print msg # that's the whole Odometry message. It should be something like
            # what was printed out by `rosmsg show nav_msgs/Odometry`
print out each of the parent variables
print "\n Parent variables: \n"
print msg.header
print msg.child_frame_id
print msg.pose
print msg.twist

print some children
print "\nSome children: \n"
print msg.header.frame_id
print msg.pose.pose
print msg.twist.twist

 print out some grandchildren
print "\nSome grandchildren: \n"
print msg.pose.pose.position
print msg.twist.twist.linear

print out some great grandchildren :)
print "\nSome great grandchildren: \n"
print msg.pose.pose.orientation.w
print msg.twist.twist.angular.z

print other (great grand) children below this line
print "\nOther ones you have specified: \n"
