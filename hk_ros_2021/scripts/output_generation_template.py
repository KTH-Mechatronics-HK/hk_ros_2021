#!/usr/bin/env python2

# Example how to generate the output file

import yaml
import rospkg
#import tagdetect				#Import the odom_tag9_subscriber node
import rospy
from std_msgs.msg import String
from apriltag_ros.msg import Coordinates



#detections = []
detections ={
             "tag_0": "None" , ##Depending on which info we decide to send from 
             "tag_1": "None" , ##shape detection/animal detection this dictionary
	     "tag_2": "None" , ##might have to be changed a bit.
	     "tag_3": "None" ,
             "tag_4": "None" ,
             "tag_5": "None" ,
             "tag_6": "None" ,
             "tag_7": "None" ,
             "tag_8": "None" ,
             "tag_9": "None" 
}
		
# 1 create an empty list to store the detections
def callback2(data):
    #print(data.data)

    xy = data.coord  #Retrieve coordinates
    tag = data.tag   #Retrieve tag number
    
    
    detections[tag] = xy  #Insert coordinates depending on tag number

    
   
# 2 append detections during the run
# remember to add logic to avoid duplicates

# first dummy detection (apriltag)
#detections.append({"obj_type": "A","Tag": tag, "XY_pos": xy})
	
    
    
# second dummy detection (geometric shape)
#detections.append({"obj_type": "B", "XY_pos": [3.396,0.123]})

# third dummy detection (animal)
#detections.append({"obj_type": "C", "XY_pos": [6.001,2.987]})

# 3 save the file
    filename = "latest_output_file.yaml"
    filepath = rospkg.RosPack().get_path('hk_ros_2021') + '/exported_detection_logs/'

    with open(filepath + filename, 'w') as outfile:
      yaml.dump(detections, outfile, default_flow_style=False)
     #yaml.dump_all(detections, outfile,explicit_start=True)
     #explicit_start=True
     
if __name__ == '__main__':


    rospy.init_node('yaml_node',anonymous = True)
    pub = rospy.Subscriber('chatter', Coordinates , callback2)

    #rate = rospy.Rate(1) # 10hz
    rospy.spin()
