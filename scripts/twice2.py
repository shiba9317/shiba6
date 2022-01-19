#!/usr/bin/env python3

# SPDX-License-Identifier: BSD-2
"""
* Copyright (C) 2020 Ryuichi Ueda. All rights reserved
"""

import rospy
from std_msgs.msg import Int 32

def cd(message):
        rospy.loginfo(message.data*2)

        if __name__== '__main__'
        rospy.init_node('twice')
        sub = rospy.Subscriber('count_up', Int 32, cd)
        rospy.spin()
