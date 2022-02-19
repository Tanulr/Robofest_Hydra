#!/usr/bin/env python
import rospy
from std_msgs.msg import String
pub = rospy.Publisher('bye', String, queue_size=10)

rospy.init_node('Node2')
rate = rospy.Rate(10) # 10hz
def publish1(name):
	hello_str = name
	rospy.loginfo(hello_str)
	pub.publish(hello_str)
	rate.sleep()
while 1:
	
	publish1("ji")

	
