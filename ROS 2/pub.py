#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
pub = rospy.Publisher('name', String, queue_size=10)
pub1 = rospy.Publisher('hello', String, queue_size=10)
rospy.init_node('Node1')
rate = rospy.Rate(10) # 10hz
def publish1(name):
	
	hello_str = name
	rospy.loginfo(hello_str)
	pub.publish(hello_str)
	rate.sleep()
def publish2(name):
	
	hello_str = name
	rospy.loginfo(hello_str)
	pub1.publish(hello_str)
	rate.sleep()	
while True:
	publish1("Hello1")
	publish2("Hello2")
	
