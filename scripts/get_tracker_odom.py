#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry

def get_current_position(msg):
    # follows the conventional x, y, poses
    twist_linear = msg.twist.twist.linear
    linear_x = twist_linear.x
    linear_y = twist_linear.y
    linear_z = twist_linear.z

    twist_angular = msg.twist.twist.angular
    angular_x = twist_angular.x
    angular_y = twist_angular.y
    angular_z = twist_angular.z

    import time
    seconds = int(round(time.time()*10))
    # time.sleep(0.5)
    # print(seconds)
    if seconds % 30 == 0:

        print("x: {:.3f} y: {:.3f} w: {:.3f}".format(linear_x, linear_y, linear_z ))
        print("x: {:.3f} y: {:.3f} w: {:.3f}".format(angular_x, angular_y, angular_z ))
        print("=======================================================================")

    else:
        pass
        


if __name__=="__main__":
    
    rospy.init_node('print_tracker_pose')
    odom_sub = rospy.Subscriber('/vive/LHR_BD4ED973_odom', Odometry, get_current_position)
    rospy.spin()
