#!/usr/bin/env python2

# Example how to generate the output file

import yaml
import rospkg
#import tagdetect				#Import the odom_tag9_subscriber node
import rospy
from std_msgs.msg import String
from apriltag_ros.msg import Coordinates
from apriltag_ros.msg import animalcoord

oldLength = -1
animaldetect = []
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
             "tag_9": "None" ,
             "boat" : "None"
}

# 1 create an empty list to store the detections
def callbackA(data):
    #print(data.data)

    xyA = data.coord  #Retrieve coordinates
    tagA = data.tag   #Retrieve tag number




    detections[tagA] = xyA  #Insert coordinates depending on tag number

# 2 append detections during the run
# remember to add logic to avoid duplicates

# first dummy detection (apriltag)
    #detections.append({"obj_type": "A","Tag": tagA, "XY_pos": xyA})

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
def callbackC(data):
    #print(data.data)

    #xyC = data.animal_coord  #Retrieve coordinates
    tagC = data.animaltag   #Retrieve tag number
    xA = data.x_coord
    yA = data.y_coord
    animaldetect.append({"XY": [xA,yA]})




    #detections[tagC] = xyC  #Insert coordinates depending on tag number

# 2 append detections during the run
# remember to add logic to avoid duplicates

# first dummy detection (apriltag)
#detections.append({"obj_type": "A","Tag": tag, "XY_pos": xy})

# second dummy detection (geometric shape)
#detections.append({"obj_type": "B", "XY_pos": [3.396,0.123]})

# third dummy detection (animal)
#detections.append({"obj_type": "C", "XY_pos": [6.001,2.987]})

# 3 save the file
    #filename = "latest_output_file.yaml"
    #filepath = rospkg.RosPack().get_path('hk_ros_2021') + '/exported_detection_logs/'#

    #with open(filepath + filename, 'w') as outfile:
      #yaml.dump(detections, outfile, default_flow_style=False)
    filename = "latest_output_file_test.yaml"
    filepath = rospkg.RosPack().get_path('hk_ros_2021') + '/exported_detection_logs/'

    with open(filepath + filename, 'w') as outfile:
      yaml.dump(animaldetect, outfile, default_flow_style=False)
     #yaml.dump_all(detections, outfile,explicit_start=True)
    # explicit_start=True
#def my_callback(event):
#    if len(animaldetect) == oldLength:
    #    return False
    #else:
    #    oldLength = len(animaldetect)
        #return True



if __name__ == '__main__':
    running = True

    rospy.init_node('yaml_node',anonymous = True)
    pubA = rospy.Subscriber('chatter', Coordinates , callbackA)
    pubC = rospy.Subscriber('animalcoord', animalcoord , callbackC)


#    running = rospy.Timer(rospy.Duration(15), my_callback)

    #if running == True:

    rospy.spin()
    #else:
        #pass#endstuff()
