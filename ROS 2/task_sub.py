import rospy
from std_msgs.msg import Int64
from std_msgs.msg import String
def function(data):
	print(str(int(data.data)**2))

rospy.init_node('subnode', anonymous = True)

rospy.Subscriber('square', String, function)
rospy.spin()
