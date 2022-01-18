#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int 32

n = 0

def cd(message):
global n
n = message.data*2

if __name__== '__main__':
rospy.init_node('twice')
sub = rospy.Subscriber('count_up', Int 32, cd)
pub = rospy.Publisher('twice', Int 32, queue_size = 1)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
pub.publish(n)
rate.sleep()
