#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Pub(Node):
    def __init__(self):
        super().__init__("pub")
        self.publisher=self.create_publisher(String,'my_topic',10)
        self.create_timer(1.0,self.pub_callback)
        self.counter=0

    def pub_callback(self):
        msg=String()
        msg.data="Hello! This is my topic. "+str(self.counter)
        self.get_logger().info(msg.data)
        self.counter+=1
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node=Pub()
    rclpy.spin(node)
    rclpy.shutdown()

