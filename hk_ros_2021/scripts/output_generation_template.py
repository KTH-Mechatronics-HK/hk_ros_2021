#!/usr/bin/env python2

# Example how to generate the output file

import yaml
import rospkg
#import tagdetect				#Import the odom_tag9_subscriber node
import rospy
from std_msgs.msg import String


detections = []

# 1 create an empty list to store the detections
def callback2(data):
    #print(data.data)
	
    xy = data.data  ##Retrieve coordinates
    print(xy)
    		#Read the return value
    #print(xy)
	#print(xy)
	#xy8 = odom_tag8_subscriber.callback8()

# 2 append detections during the run
# remember to add logic to avoid duplicates

# first dummy detection (apriltag)
    detections.append({"obj_type": "A", "XY_pos": xy})
	#detections.append({"obj_type": "A8", "XY_pos": xy8})



# second dummy detection (geometric shape)
#detections.append({"obj_type": "B", "XY_pos": [3.396,0.123]})

# third dummy detection (animal)
#detections.append({"obj_type": "C", "XY_pos": [6.001,2.987]})

# 3 save the file
    filename = "latest_output_file.yaml"
    filepath = rospkg.RosPack().get_path('hk_ros_2021') + '/exported_detection_logs/'

    with open(filepath + filename, 'w') as outfile:
      yaml.dump_all(detections, outfile,explicit_start=True)
if __name__ == '__main__':

    
    rospy.init_node('yaml_node',anonymous = True)
    pub = rospy.Subscriber('chatter', String , callback2)

    #rate = rospy.Rate(1) # 10hz
    rospy.spin()
