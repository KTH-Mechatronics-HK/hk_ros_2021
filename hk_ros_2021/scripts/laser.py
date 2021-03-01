#! /usr/bin/env python
import math
import rospy
import tf
import tf2_ros

from sensor_msgs.msg import LaserScan



def callback2(laserData): #function for determining laser distance at determined angle
#    print len(msg.ranges)


    try:
        if lidar_angle == 500:
            return

        lidar_angle_new = int(lidar_angle)
        print(lidar_angle_new)
    except NameError:
        return

    animalDistance = laserData.ranges[lidar_angle_new]
    print(animalDistance)
    #lidar_angle = 500
    #animalDistance = laserData.ranges[int(lidar_angle)]
    #lidar_angle = None
    #print(animalDistance)

    # if lidar_angle:
    #     print(lidar_angle)

    # try:
    #     animal_distance = laserData.ranges[lidar_angle]
    # # if x_angle:
    #     print(animal_distance)
    #
    # except(IndexError):
    #pub = rospy.Publisher('animalFound', Coordinates, queue_size=10)
    #return

if __name__ == '__main__':



    #sub1 = rospy.Subscriber('/darknet_ros/bounding_boxes', BoundingBoxes , callback1)
    sub2 = rospy.Subscriber('/scan', LaserScan , callback2)
    # sub3 = rospy.Subscriber('chatter', Coordinates , callback2)

    rospy.spin() #continuous loop
