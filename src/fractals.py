#!/usr/bin/python

from geometry_msgs.msg import Twist
import rospy

class Fractals(object):

    def init(self):
        self.publisher = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
        self.twist = Twist()

    def reset_twist(self):
        self.twist.linear.x = 0.0
        self.twist.linear.y = 0.0
        self.twist.linear.z = 0.0
        self.twist.angular.x = 0.0
        self.twist.angular.y = 0.0
        self.twist.angular.z = 0.0

    def run(self):
		self.init()
		self.counter = 0
		while not rospy.is_shutdown():
		    self.twist.linear.x = 1
		    self.publisher.publish(self.twist)
		    rospy.sleep(1)
		    self.reset_twist()
		    self.twist.angular.z = 1.05
		    self.publisher.publish(self.twist)
		    rospy.sleep(1)
		    self.reset_twist()
		    self.twist.linear.x = 1
		    self.publisher.publish(self.twist)
		    rospy.sleep(1)
		    self.reset_twist()
		    self.twist.angular.z = -2.1
		    self.publisher.publish(self.twist)
		    rospy.sleep(1)
		    self.reset_twist()
		    self.twist.linear.x = 1
		    self.publisher.publish(self.twist)
		    rospy.sleep(1)
		    self.reset_twist()
		    self.twist.angular.z = 1.05
		    self.publisher.publish(self.twist)
		    rospy.sleep(1)
		    self.reset_twist()
		    self.twist.linear.x = 1
		    self.publisher.publish(self.twist)
		    rospy.sleep(1)
		    self.reset_twist()
		    self.twist.angular.z = 1.05
		    self.publisher.publish(self.twist)
		    self.counter +=1
		    if self.counter == 6:
		    	break

if __name__ == "__main__":
    rospy.init_node("fractals_drawer")
    fractals = Fractals()
    fractals.run()