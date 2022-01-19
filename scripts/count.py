#!/usr/bin/env python3

# SPDX-License-Identifier: BSD-2
"""
* Copyright (C) 2020 Ryuichi Ueda. All rights reserved
"""

import rospy
from std_msgs.msg import Int 32

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int 32, queue_size = 1)
rate = rospy.Rate(10)
        n = 0
        while not rospy.is_shutdown():
                n += 1
                pub.publish(n)
                rate.sleep()
