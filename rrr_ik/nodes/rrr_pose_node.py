#!/usr/bin/python

"""
Write ROS node to publish Pose2D
"""

import rospy
from geometry_msgs.msg import Pose2D

def talker():
    pub = rospy.Publisher('des_pose', Pose2D, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        des_pos = Pose2D()
        des_pos.x = 1
        des_pos.y = 1
        des_pos.theta = 0.2
        rospy.loginfo(des_pos)
        pub.publish(des_pos)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass