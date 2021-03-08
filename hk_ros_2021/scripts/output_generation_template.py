#!/usr/bin/env python2

# Example how to generate the output file

import yaml
import rospkg
#import tagdetect				#Import the odom_tag9_subscriber node
import rospy
from std_msgs.msg import String
from apriltag_ros.msg import Coordinates
from apriltag_ros.msg import animalcoord
from apriltag_ros.msg import geometriccoords
import math
#import statistics
import statistics
import numpy

oldLength = -1
animaldetect = []
geometricdetect = []
#detections = []
detections ={
             #"tag_0": "None" , ##Depending on which info we decide to send from
             #"tag_1": "None" , ##shape detection/animal detection this dictionary
	        # "tag_2": "None" , ##might have to be changed a bit.
	        # "tag_3": "None" ,
             #"tag_4": "None" ,
            # "tag_5": "None" ,
            # "tag_6": "None" ,
            # "tag_7": "None" ,
            # "tag_8": "None" ,
            # "tag_9": "None" ,
            # "boat" : "None"


}


result = []
result2 = []

resultgeo = []
resultgeo2 = []

# 1 create an empty list to store the detections
def callbackA(data):
    #print(data.data)


    xA = data.x_coord
    yA = data.y_coord

    tagA = data.tag   #Retrieve tag number





    detections[tagA] = [xA,yA]  #Insert coordinates depending on tag number



# 3 save the file
    filename = "latest_output_file_apriltags.yaml"
    filepath = rospkg.RosPack().get_path('hk_ros_2021') + '/exported_detection_logs/'

    with open(filepath + filename, 'w') as outfile:
      yaml.dump(detections, outfile, default_flow_style=False)


def endstuffA():
    goaldict = []
    filename = "latest_output_file.yaml"
    filepath = rospkg.RosPack().get_path('hk_ros_2021') + '/exported_detection_logs/'
    outfile = open(filepath + filename, 'w')

    for key in detections:
        a = detections[key][0]
        b = detections[key][1]

        goaldict.append({"obj_type": "A", "XY_pos": [a,b]})

        #filename = "latest_output_file.yaml"
        #filepath = rospkg.RosPack().get_path('hk_ros_2021') + '/exported_detection_logs/'


    yaml.dump_all(goaldict, outfile, explicit_start=True)

    outfile.close()

def callbackB(data):

    xB = data.x_geometric
    yB = data.y_geometric

    geometricdetect.append([xB,yB])

def endstuffB():
    print("entered")
    n = 0
    k = 0
    previous = [0,0]
    previous2 = [0,0]
    targetg = []

    geometricdetect.append([0,0])
    for detection in geometricdetect:
        #print(detection)
        if n ==0:
            previous = detection
            targetg.append(detection)

            n = n+1
            continue
        if (abs(previous[0]-detection[0]) <= 0.3) and (abs(previous[1]-detection[1]) <= 0.3):

            targetg.append(detection)

        else:
            previous = detection
            if len(targetg) > 1:
                x = statistics.median([coord[0] for coord in targetg])
                y = statistics.median([coord[1] for coord in targetg])
                #x = target[len(target)-1][0]
                #y = target[len(target)-1][1]
                #print(x)
                #print(y)
                resultgeo.append([x,y])

            targetg = []


    #x = statistics.median([coord[0] for coord in target])
    #y = statistics.median([coord[1] for coord in target])
    #resultgeo.append([x,y])


    for detection in resultgeo:
        x = detection[0]
        y = detection[1]
        flag = False
        if k == 0:
            resultgeo2.append([x,y])
            flag = True
            k = k+1
        for prev in resultgeo2:
            if (abs(prev[0]-x) <= 0.5) and (abs(prev[1]-y) <= 0.5):#(abs(result[k][0]-x) <= 0.3) and (abs(result[k][1]-y) <= 0.3):
                flag = True
        if flag == False:
            resultgeo2.append([x,y])

    filename = "latest_output_file_geometric.yaml"
    filepath = rospkg.RosPack().get_path('hk_ros_2021') + '/exported_detection_logs/'

    with open(filepath + filename, 'w') as outfile:
      yaml.dump_all(resultgeo2, outfile, explicit_start=True)
    print(resultgeo2)

    goaldict = []
    for goal in resultgeo2:
        goaldict.append({"obj_type": "B", "XY_pos": [goal[0],goal[1]]})
        filename = "latest_output_file.yaml"
        filepath = rospkg.RosPack().get_path('hk_ros_2021') + '/exported_detection_logs/'
        with open(filepath + filename, 'a') as outfile:
          yaml.dump_all(goaldict, outfile, explicit_start=True)
        goaldict = []






def callbackC(data):
    #print(data.data)



    #xyC = data.animal_coord  #Retrieve coordinates
    tagC = data.animaltag   #Retrieve tag number
    xA = data.x_coord
    yA = data.y_coord
    animaldetect.append([xA,yA])


def endstuffC():
    print("entered")
    n = 0
    k = 0
    previous = [0,0]
    previous2 = [0,0]
    target = []
    target2 = []
    animaldetect.append([0,0])
    for detection in animaldetect:
        #print(detection)
        if n ==0:
            previous = detection
            target.append(detection)

            n = n+1
            continue
        if (abs(previous[0]-detection[0]) <= 0.3) and (abs(previous[1]-detection[1]) <= 0.3):

            target.append(detection)

        else:
            previous = detection
            if len(target) > 1:
                x = statistics.median([coord[0] for coord in target])
                y = statistics.median([coord[1] for coord in target])
                #x = target[len(target)-1][0]
                #y = target[len(target)-1][1]
                #print(x)
                #print(y)
                result.append([x,y])

            target = []

    #x = statistics.median([coord[0] for coord in target])
    #y = statistics.median([coord[1] for coord in target])
    #result.append([x,y])


    for detection in result:
        x = detection[0]
        y = detection[1]
        flag = False
        if k == 0:
            result2.append([x,y])
            flag = True
            k = k+1
        for prev in result2:
            if (abs(prev[0]-x) <= 0.5) and (abs(prev[1]-y) <= 0.5):#(abs(result[k][0]-x) <= 0.3) and (abs(result[k][1]-y) <= 0.3):
                flag = True
        if flag == False:
            result2.append([x,y])




    print(result)
    filename = "latest_output_file_animal.yaml"
    filepath = rospkg.RosPack().get_path('hk_ros_2021') + '/exported_detection_logs/'

    with open(filepath + filename, 'w') as outfile:
      yaml.dump_all(result2, outfile, explicit_start=True)

    goaldict = []
    for goal in result2:
        goaldict.append({"obj_type": "C", "XY_pos": [goal[0],goal[1]]})

        filename = "latest_output_file.yaml"
        filepath = rospkg.RosPack().get_path('hk_ros_2021') + '/exported_detection_logs/'

        with open(filepath + filename, 'a') as outfile:
            yaml.dump_all(goaldict, outfile, explicit_start=True)
        goaldict =[]




if __name__ == '__main__':
    running = True

    rospy.init_node('yaml_node',anonymous = True)
    pubA = rospy.Subscriber('AprilTag_chatter', Coordinates , callbackA)
    pubB = rospy.Subscriber('Shape_chatter', geometriccoords , callbackB)
    pubC = rospy.Subscriber('Animal_chatter', animalcoord , callbackC)


    rospy.sleep(252.2)  #209
    print("Got to end")
    endstuffA()
    endstuffB()
    endstuffC()



#    running = rospy.Timer(rospy.Duration(15), my_callback)

    #if running == True:

    rospy.spin()
    #else:
        #pass#endstuff()
