#!/usr/bin/python
"""
ROS node for inverse kinematics of planar 3R robot arm using numpy
"""

import rospy
import numpy as np
from std_msgs.msg import Float64, Float64MultiArray
from std_msgs.msg import Bool
from geometry_msgs.msg import Pose2D
from math import *

class IK_3R_Robot:
    def __init__(self):
        # Initialize node
        rospy.init_node('IK_3R_Robot', anonymous=True)
        # Create publisher
        self.pub = rospy.Publisher('joint_states', Float64MultiArray, queue_size=10)
        # Create subscriber
        self.sub = rospy.Subscriber('des_pose', Pose2D, self.callback)

        # Create a timer that calls the cbTimer function every 1.0 second
        self.timer = rospy.Timer(rospy.Duration(1.0), self.cbTimer)
        # Lengths
        self.l1, self.l2, self.l3 = 1, 0.5, 0.2
        # IK Solutions (in radians)
        self.q1, self.q2, self.q3 = [None] * 3

    def cbTimer(self, event):
        # Create a message to publish
        msg = Float64MultiArray()
        msg.data.extend([self.q1, self.q2, self.q3])
        # Publish the message
        self.pub.publish(msg)

    def callback(self, msg):
        """Inverse kinematics for a 3R arm derived"""
        x = msg.x
        y = msg.y
        theta = msg.theta
        # Code BEGIN
        
        

        # Code END
        print([x, y, theta])
        

if __name__ == '__main__':
    try:
        IK_3R_Robot()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass