#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Circular(Node):
    def __init__(self):
        super().__init__("move_circular")
        self.publisher=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.create_timer(0.5,self.pub_callback)


    def pub_callback(self):
        msg=Twist()
        msg.linear.x=1.0
        msg.linear.y=1.0
        msg.angular.z=1.0
        self.publisher.publish(msg)

def main():
    rclpy.init()
    node=Circular()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()