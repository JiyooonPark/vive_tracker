#!/usr/bin/env python3

'''
0.2 = 20cm
1 = 1m
the y is wrong 
'''
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
i=0  
position_0 = []
position_1 = []
def get_current_position(msg):
    global position_0, position_1
    # follows the conventional x, y, poses
    pose_position = msg.pose.pose.position
    position_x = pose_position.x
    position_y = pose_position.y
    position_z = pose_position.z

    pose_orientation = msg.pose.pose.orientation
    orientation_x = pose_orientation.x
    orientation_y = pose_orientation.y
    orientation_z = pose_orientation.z

    # import time
    # seconds = int(round(time.time()*10))
    # if seconds % 10 == 0:

    #     print("x: {:.3f} y: {:.3f} w: {:.3f}".format(position_x, position_y, position_z ))
    #     print("x: {:.3f} y: {:.3f} w: {:.3f}".format(orientation_x, orientation_y, orientation_z ))
    #     print("=======================================================================")

    # else:
    #     pass
    global i 
    i+=1
    if i<=10:
        position_0 = [position_x, position_y, position_z]
        position_1 = [position_x, position_y, position_z]
    else:
        position_1 = [position_x, position_y, position_z]
    print(f'position0: {position_0},  position_final: {position_1}')
    print(f'x: {round(position_1[0]-position_0[0], 3)}, y: {round(position_1[1]-position_0[1], 3)}, z: {round(position_1[2]-position_0[2], 3)}')


if __name__=="__main__":
    
    rospy.init_node('print_tracker_pose')
    odom_sub = rospy.Subscriber('/vive/LHR_2FCD60B0_pose', PoseWithCovarianceStamped, get_current_position)
    rospy.spin()
