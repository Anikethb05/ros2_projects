#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Sub(Node):
    def __init__(self):
        super().__init__("sub")
        self.subscriber=self.create_subscription(String,"my_topic",self.sub_callback,10)

    def sub_callback(self, msg: String):
        self.get_logger().info("I recieved: "+msg.data)

def main(args=None):
    rclpy.init(args=args)
    node=Sub()
    rclpy.spin(node)
    rclpy.shutdown()