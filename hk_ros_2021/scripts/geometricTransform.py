#!/usr/bin/env python
import rospy
import tf2_ros
import tf2_msgs.msg
import geometry_msgs.msg
from apriltag_ros.msg import animalpixels
from apriltag_ros.msg import geometricrelcoords

def callback(coordinates):

    x = coordinates.geometricrel_x

    y = coordinates.geometricrel_y
    #print(x)
    #print(y)
    tfb = FixedTFBroadcaster(x,y)

class FixedTFBroadcaster:

    def __init__(self,x,y):
        self.pub_tf = rospy.Publisher("/tf", tf2_msgs.msg.TFMessage, queue_size=1)

        #while not rospy.is_shutdown():
            # Run this loop at about 10Hz
        rospy.sleep(0.1)

        t = geometry_msgs.msg.TransformStamped()
        t.header.frame_id = "base_scan"
        t.header.stamp = rospy.Time.now()
        t.child_frame_id = "geometrictag"
        t.transform.translation.x = x#x
        t.transform.translation.y = y#y
        t.transform.translation.z = 0.0

        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1

        tfm = tf2_msgs.msg.TFMessage([t])
        self.pub_tf.publish(tfm)

if __name__ == '__main__':
    rospy.init_node('fixed_tf2_broadcaster_geo')
    pub = rospy.Subscriber('Shape_info', geometricrelcoords , callback)

    #tfb = FixedTFBroadcaster()

    rospy.spin()
