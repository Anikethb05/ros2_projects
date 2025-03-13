#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math


class Shape(Node):
    def __init__(self):
        super().__init__("shape")
        self.pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.create_timer(1.0,self.shape_callback)
        self.step=0
        self.turn=0

    def shape_callback(self):
        cmd=Twist()
        if self.step % 2 == 0:  # Move forward
            cmd.linear.x = 2.0
            cmd.angular.z = 0.0
        else:  # Turn 90 degrees
            cmd.linear.x = 0.0
            cmd.angular.z = 2*math.pi/3  # 90 degrees

        self.pub.publish(cmd)
        self.step += 1
            

def main(args=None):
    rclpy.init(args=args)
    node=Shape()
    rclpy.spin(node)
    rclpy.shutdown()