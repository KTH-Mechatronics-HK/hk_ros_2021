#!/usr/bin/env python
import rospy
import math
import tf
import geometry_msgs.msg
import tf2_ros
#from nav_msgs.msg import Odometry
#from tf.msg import tfMessage

#from apriltag_ros import ApriltagDetectionArray
#from geometry_msgs import PoseWithCovariance
#from AprilTagDetectionArray.msg import AprilTagDetection
#include <apriltags_ros/AprilTagDetectionArray.h>
from apriltag_ros.msg import AprilTagDetectionArray
from tf2_msgs.msg import TFMessage




def callback(detectionarray):

    #pub = rospy.Subscriber('tag_detections', AprilTagDetection , chatter_callback)
    rospy.init_node('odom_tag9',anonymous = True)
    #msg = rospy.wait_for_message("/tag_detections", Pose)

    list = tf.TransformListener()
    #rate = rospy.Rate(1) # 10hz

    #rate = rospy.Rate(1) #one message per second
    try:
        frame_id = str(detectionarray.detections[0].id)
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException, IndexError):
        return


    tag_frame = "tag_"+frame_id[1:2]        #Getting the number out of frame_id
    print(frame_id)
    print(tag_frame)

    #listener.waitForTransform('/odom', tag, rospy.Time(), rospy.Duration(60))

    #while not rospy.is_shutdown():
        #try:
    #try:
    #rospy.sleep(10.0)
    (trans,rot) = list.lookupTransform( '/odom','/tag_9' , rospy.Time(0))
    #x = str(trans[0]*(-1))            #Multiply with -1 to transform the given coordinates
    #y = str(trans[1]*(-1))            #to match the odom frame orientation
    print trans

    #except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException, IndexError):
        #pass

        #print '[',trans[0]*(-1),',',trans[1]*(-1),']'

        #x = str(trans[0]*(-1))            #Multiply with -1 to transform the given coordinates
        #y = str(trans[1]*(-1))            #to match the odom frame orientation
    #oordinates = (x + ", " + y)

        #rate.sleep()
	#print coordinates
	#return coordinates

def listener():
   #try:
	   #rospy.init_node('odom_tag9',anonymous = True)
        rospy.init_node('odom_tag9',anonymous = True)
        list = tf.TransformListener()
        pub = rospy.Subscriber('/tf', TFMessage)
        pub = rospy.Subscriber('/tag_detections', AprilTagDetectionArray , callback)

   #rate = rospy.Rate(1) # 10hz
        rospy.spin()
   #except rospy.ROSInterrupException:
      #rospy.loginfo("node terminated.")

if __name__ == '__main__':
    listener()

#for i = 1:N
 #   tag_data.t(i) = getBagTime(tag_msg{i})-t0;
  #  for j = 1:numel(tag_msg{i}.detections)
   #     detection = tag_msg{i}.detections(j);
    #    if numel(detection.id)>1
     #       % Can only use standalone tag detections for calibration!
      #      % The math allows for bundles too (e.g. bundle composed of
       ##    % anyway
         #   warning_str = 'Skipping tag bundle detection with IDs';
          #  for k = 1:numel(detection.id)
           #     warning_str = sprintf('%s %d',warning_str,detection.id(k));
#            end
 #           warning(warning_str);
 #           continue;
#        end
#        tag_data.detection(i).id(j) = detection.id;
#        tag_data.detection(i).size(j) = detection.size;
#        % Tag position with respect to camera frame
#        tag_data.detection(i).p(:,j) = detection.pose.pose.pose.position;
#        % Tag orientation with respect to camera frame
#        % [w;x;y;z] format
#        tag_data.detection(i).q(:,j) = ...
 #                        detection.pose.pose.pose.orientation([4,1,2,3]);
#    end


#https://robotics.stackexchange.com/questions/20854/get-topic-values-in-script
