#!/usr/bin/env python2

# DESCRIPTION: 
# Evaluation script for autonomous inspection task of HK2021
#
# Scoring rules:
# if two detections are within scoring range of a gt detection only the closest one will be scored for that gt detection 
# if a detection is within scoring range of two gt detections, both will be counted (however this should rarely happen since the gt dets of the same class are typically more than 2m apart) 
# only the first len(dets_gt) detections will be counted (to prevent cheating by just randomly placing objects)

# Scoring parameters
base_score_A = 1000
base_score_B = 500
base_score_C = 250
threshold_full_score = 0.2 # m, full score will be awarded for detections within this threshold
threshold_half_score = 0.5 # m, half score will be awarded for detections within this threshold
threshold_quart_score = 1.0 # m, a quarder score will be awarded for detections within this threshold
help_by_rot = True # if help_by_rot param is set to true, we compute scores for a bunch of initial orientations and select the highest scoring one
high_dpi_screen = True

import yaml
import numpy as np
import copy
import Tkinter, tkFileDialog
#import matplotlib
#matplotlib.use('Qt5Agg')
import matplotlib.pylab as plt

if(high_dpi_screen):
    plt.rcParams['figure.dpi'] = 200 # default 100
    plt.rcParams['figure.figsize'] = 8, 8
plt.close()

def compute_score(dets_gt,dets_eval):

    # outer loop over gt detections
    scores = []
    for i in range(len(dets_gt)):
        det_gt = dets_gt[i]
    
        # inner loop over eval detections
        mindist = np.inf
        #idx_of_min = None
        for j in range(len(dets_eval)):
            det_eval = dets_eval[j]
                        
            if(det_gt["obj_type"] == det_eval["obj_type"]):
                dist = np.linalg.norm(np.atleast_2d(det_gt["XY_pos"]) - np.atleast_2d(det_eval["XY_pos"]))
                if (dist < mindist):
                    mindist = dist
                    #idx_of_min = j
        
        # set base score based on object type
        if(det_gt["obj_type"] == "A"):
            base_score = base_score_A
        elif(det_gt["obj_type"] == "B"):
            base_score = base_score_B
        elif(det_gt["obj_type"] == "C"):
            base_score = base_score_C
    
        # give score deduction based on mindist
        if (mindist < threshold_full_score):
            det_score = base_score
        elif(mindist < threshold_half_score):
            det_score = base_score/2.0
        elif(mindist < threshold_quart_score):
            det_score = base_score/4.0
        else:
            det_score = 0
        
        # add det score to total
        scores.append(det_score)
        
    return scores

# START
# load GT
stream = open("ground_truth2.yaml", "r")
yamldocs_gt = yaml.load_all(stream,Loader=yaml.SafeLoader)

dets_gt = []
for entry in yamldocs_gt: 
    dets_gt.append(entry)

# load file to be evaluated (add last)
root = Tkinter.Tk()
root.withdraw()
file_to_eval = tkFileDialog.askopenfilename()
root.destroy()

stream = open(file_to_eval, "r")
yamldocs_eval = yaml.load_all(stream,Loader=yaml.SafeLoader)
dets_eval = []
for entry in yamldocs_eval: 
    if (len(dets_eval) < len(dets_gt)):   
        dets_eval.append(entry)


# first check input file on correct format
for det_eval in dets_eval:
    if (det_eval["obj_type"] not in ["A","B","C"]):
        print "WARNING! Faulty obj_type"


# compute the scores
if(help_by_rot): 
    yaw_init_arr = np.linspace(-3.14,3.14,1000)
    total_scores_rot = []
    best_total_score_rot = 0
    for yaw_init in yaw_init_arr:
        # rotate det_eval
        dets_eval_rot = copy.deepcopy(dets_eval) 
        for i in range(len(dets_eval)):
            dets_eval_rot[i]["XY_pos"][0] = dets_eval[i]["XY_pos"][0]*np.cos(yaw_init) - dets_eval[i]["XY_pos"][1]*np.sin(yaw_init)
            dets_eval_rot[i]["XY_pos"][1] = dets_eval[i]["XY_pos"][0]*np.sin(yaw_init) + dets_eval[i]["XY_pos"][1]*np.cos(yaw_init)
        # compute score
        scores = compute_score(dets_gt,dets_eval_rot)
        total_score_rot = np.array(scores).sum()
        total_scores_rot.append(total_score_rot) 
        
        if(total_score_rot > best_total_score_rot):
            best_total_score_rot = total_score_rot
            yaw_init_best = yaw_init
            dets_eval_best = copy.deepcopy(dets_eval_rot)
    dets_eval_toscore = copy.deepcopy(dets_eval_best)
    
else:
    dets_eval_toscore = copy.deepcopy(dets_eval)

scores = compute_score(dets_gt,dets_eval_toscore)
total_score = np.array(scores).sum()




### PRINT ###
for i in range(len(scores)):
    print "Score for gt det " + str(i) + ": " + str(scores[i])
print "TOTAL SCORE FOR FILE " + str(file_to_eval) + ": " + str(total_score)


### PLOT ###

# initial robot pose
fig, ax = plt.subplots()
ax.plot(0,0, 'b>', markersize=12)

# gt detections
for det in dets_gt:
    if(det["obj_type"] == "A"):
        markerstyle = "bo"
        mA, = ax.plot(det["XY_pos"][0],det["XY_pos"][1], markerstyle)
    elif(det["obj_type"] == "B"):
        markerstyle = "ro"
        mB, = ax.plot(det["XY_pos"][0],det["XY_pos"][1], markerstyle)
    elif(det["obj_type"] == "C"):
        markerstyle = "go"
        mC, = ax.plot(det["XY_pos"][0],det["XY_pos"][1], markerstyle)  

# eval detections
for det in dets_eval_toscore:
    if(det["obj_type"] == "A"):
        markerstyle = "bx"
        ax.plot(det["XY_pos"][0],det["XY_pos"][1], markerstyle)
    elif(det["obj_type"] == "B"):
        markerstyle = "rx"
        ax.plot(det["XY_pos"][0],det["XY_pos"][1], markerstyle)
    elif(det["obj_type"] == "C"):
        markerstyle = "gx"
        ax.plot(det["XY_pos"][0],det["XY_pos"][1], markerstyle)
    else:
        print "WARNING! Faulty obj_type in eval file"

ax.set_title('SCORE: ' + str(total_score))        
ax.legend((mA, mB, mC), ('A', 'B', 'C'))
ax.set_aspect('equal', 'box') 
plt.show()


