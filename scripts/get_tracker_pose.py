#!/usr/bin/env python3

'''
0.2 = 20cm
1 = 1m
the y is wrong 
'''
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

def get_current_position(msg):
    # follows the conventional x, y, poses
    pose_position = msg.pose.pose.position
    position_x = pose_position.x
    position_y = pose_position.y
    position_z = pose_position.z

    pose_orientation = msg.pose.pose.orientation
    orientation_x = pose_orientation.x
    orientation_y = pose_orientation.y
    orientation_z = pose_orientation.z

    import time
    seconds = int(round(time.time()*10))
    # time.sleep(0.5)
    # print(seconds)
    if seconds % 10 == 0:

        print("x: {:.3f} y: {:.3f} w: {:.3f}".format(position_x, position_y, position_z ))
        print("x: {:.3f} y: {:.3f} w: {:.3f}".format(orientation_x, orientation_y, orientation_z ))
        print("=======================================================================")

    else:
        pass
        


if __name__=="__main__":
    
    rospy.init_node('print_tracker_pose')
    odom_sub = rospy.Subscriber('/vive/LHR_BD4ED973_pose', PoseWithCovarianceStamped, get_current_position)
    rospy.spin()
