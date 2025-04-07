#!/bin/python3

import rclpy
from rclpy.node import Node

class HelloWorld(Node):
    def __init__(self):
        super().__init__("hello_node")
        self.counter=0
        self.create_timer(1,self.hello_callback)
        #self.get_logger().info("Hello")

    def hello_callback(self):
        self.get_logger().info("Hello "+ str(self.counter))
        self.counter+=1


def main(args=None):
    rclpy.init(args=args)

    #code
    node=HelloWorld()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=='__main__':
    main()