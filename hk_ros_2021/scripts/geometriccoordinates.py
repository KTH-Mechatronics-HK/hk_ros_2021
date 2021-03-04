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

from apriltag_ros.msg import geometriccoords
from apriltag_ros.msg import geometricrelcoords


from std_msgs.msg import String


rospy.init_node('Coordinates_geometric',anonymous = True)
list = tf.TransformListener()

def callback(geometric):


    #pub = rospy.Subscriber('tag_detections', AprilTagDetection , chatter_callback)
    #rospy.init_node('odom_tag9',anonymous = True)
    #msg = rospy.wait_for_message("/tag_detections", Pose)
    pub = rospy.Publisher('geometriccoord', geometriccoords, queue_size=10)  #Create a chatter node, so we can retrieve coordinates into yaml file
    #rospy.init_node('talker', anonymous=True)
    #list = tf.TransformListener()
    #rate = rospy.Rate(1) # 10hz

    #rate = rospy.Rate(1) #one message per second

    try:

        list.waitForTransform('/odom', '/geometrictag' ,rospy.Time(), rospy.Duration(1)) #Waiting for a bit to get rid of errors
        (trans,rot) = list.lookupTransform( '/static_frame','/geometrictag' , rospy.Time(0)) #performing the transformation

        #x = str(trans[0])            #Multiply with -1 to transform the given coordinates
        #y = str(trans[1])            #to match the odom frame orientation

        x = trans[0]
        y = trans[1]
        #print(x)
        #print(y)
        #coordinates = (x + ", " + y)  #Combining x and y coordinates into a string
        #print(coordinates)
        #return coordinates

    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException, IndexError):
        return
    #return coordinates

    geometric = geometriccoords()

    #animal.animal_coord = coordinates
    geometric.x_geometric = x
    geometric.y_geometric = y



    try:
        pub.publish(geometric)   #Publishing coordinates onto the "chatter" topic for the yaml file to read.

    except rospy.ROSInterruptException:
        pass




if __name__ == '__main__':

    #rospy.init_node('odom_tag9',anonymous = True)

    sub1 = rospy.Subscriber('/geometric_info', geometricrelcoords , callback)

   #rate = rospy.Rate(1) # 10hz
    rospy.spin()
