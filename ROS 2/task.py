import rospy
from std_msgs.msg import Int64
from std_msgs.msg import String
pub = rospy.Publisher('square', String, queue_size=10)
rospy.init_node('pubnode')
rate = rospy.Rate(10) # 10hz
def num(x):
	rospy.loginfo(str(x))
	pub.publish(str(x))
	rate.sleep()
a=0
while True:
	num(a)
	a=a+1
