import rospy
from std_msgs.msg import String

def function(data):
	print(data.data)

rospy.init_node('node3', anonymous = True)

rospy.Subscriber('name', String, function)
rospy.Subscriber('hello', String, function)
rospy.Subscriber('bye', String, function)
rospy.spin()
