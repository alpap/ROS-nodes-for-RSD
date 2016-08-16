#!/usr/bin/env python
# license removed for brevity
import rospy
import time

from std_msgs.msg import String
# from std_msgs.msg import UInt32
# from std_msgs.msg import Bool

import serial

ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)

def callback(data):
	ser.write(str(data.data) + "\0")

def listener():
    
    
	rospy.Subscriber("serial_com", String, callback)
	
    #rate = rospy.Rate(10)
    #while not rospy.is_shutdown():
	
	SafetyOn = ser.read()
	pub.publish(SafetyOn)

	print SafetyOn
	SafetyOn = ser.read()
	pub.publish(SafetyOn)

	print SafetyOn
	SafetyOn = ser.read()
	pub.publish(SafetyOn)

	print SafetyOn
	SafetyOn = ser.read()
	pub.publish(SafetyOn)

	print SafetyOn
	#rospy.spin()
	#rate.sleep()
    #rospy.spin()
	

if __name__ == '__main__':
	rospy.init_node('safty_node', anonymous=True)
	pub = rospy.Publisher('/Safty_node_chatter', String, queue_size=1)
	ser.write("s")
	listener()
	rospy.spin()
	ser.close()

