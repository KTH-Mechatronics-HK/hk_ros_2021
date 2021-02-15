#!/usr/bin/env python2

# Example how to generate the output file

import yaml
import rospkg
#import odom_tag9_subscriber 				#Import the odom_tag9_subscriber node
import rospy
#import odom_tag8_subscriber
from std_msgs.msg import String
detections = []



def callback2(data):

	my_data = data.data
# 1 create an empty list to store the detections
	while(1):
	#xy = odom_tag9_subscriber.callback()  		#Read the return value
	#xy8 = odom_tag8_subscriber.callback8()
	#msg = rospy.wait_for_message("/std_msgs.msg", String)
	#cord = msg.coordinate
# 2 append detections during the run
# remember to add logic to avoid duplicates

# first dummy detection (apriltag)
		detections.append({"obj_type": "A9", "XY_pos": my_data})
	#detections.append({"obj_type": "A9", "XY_pos": xy8})

	

# second dummy detection (geometric shape)
#detections.append({"obj_type": "B", "XY_pos": [3.396,0.123]})

# third dummy detection (animal)
#detections.append({"obj_type": "C", "XY_pos": [6.001,2.987]})   
    
# 3 save the file
		filename = "latest_output_file.yaml"
		filepath = rospkg.RosPack().get_path('hk_ros_2021') + '/exported_detection_logs/' 

		with open(filepath + filename, 'w') as outfile:
    	   		yaml.dump_all(detections, outfile,explicit_start=True)




def listener():
	rospy.init_node('listener', anonymous=True)

        rospy.Subscriber("chatter", String, callback2)

if __name__ == '__main__':
    listener()



