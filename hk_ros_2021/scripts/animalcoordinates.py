#! /usr/bin/env python


import rospy
import math
import tf
import geometry_msgs.msg
import tf2_ros
from std_msgs.msg import String
#from nav_msgs.msg import Odometry
#from tf.msg import tfMessage

#from apriltag_ros import ApriltagDetectionArray
#from geometry_msgs import PoseWithCovariance
#from AprilTagDetectionArray.msg import AprilTagDetection
#include <apriltags_ros/AprilTagDetectionArray.h>
from apriltag_ros.msg import AprilTagDetectionArray
from apriltag_ros.msg import animalpixels
from apriltag_ros.msg import animalcoord

from std_msgs.msg import String


rospy.init_node('Animalcoords',anonymous = True)
list = tf.TransformListener()

def callback(animal_geometric):


    #pub = rospy.Subscriber('tag_detections', AprilTagDetection , chatter_callback)
    #rospy.init_node('odom_tag9',anonymous = True)
    #msg = rospy.wait_for_message("/tag_detections", Pose)
    pub = rospy.Publisher('Animal_chatter', animalcoord, queue_size=10)  #Create a chatter node, so we can retrieve coordinates into yaml file
    #rospy.init_node('talker', anonymous=True)
    #list = tf.TransformListener()
    #rate = rospy.Rate(1) # 10hz
    animaltag = animal_geometric.animaltag
    print(animaltag)
    #rate = rospy.Rate(1) #one message per second

    try:

        list.waitForTransform('/odom', '/animaltag' ,rospy.Time(), rospy.Duration(1)) #Waiting for a bit to get rid of errors
        (trans,rot) = list.lookupTransform( '/static_frame','/animaltag' , rospy.Time(0)) #performing the transformation

        #x = str(trans[0])            #Multiply with -1 to transform the given coordinates
        #y = str(trans[1])            #to match the odom frame orientation

        x = trans[0]
        y = trans[1]
        #coordinates = (x + ", " + y)  #Combining x and y coordinates into a string
        #print(coordinates)
        #return coordinates

    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException, IndexError):
        return
    #return coordinates

    animal = animalcoord()

    #animal.animal_coord = coordinates
    animal.x_coord = x
    animal.y_coord = y
    animal.animaltag = animal_geometric.animaltag


    try:
        pub.publish(animal)   #Publishing coordinates onto the "chatter" topic for the yaml file to read.

    except rospy.ROSInterruptException:
        pass


































if __name__ == '__main__':

    #rospy.init_node('odom_tag9',anonymous = True)

    sub1 = rospy.Subscriber('/Animal_info', animalpixels , callback)

   #rate = rospy.Rate(1) # 10hz
    rospy.spin()
