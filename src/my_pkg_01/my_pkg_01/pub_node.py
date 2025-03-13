#!/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyPublisher(Node):
    def __init__(self):
        super().__init__("pub_node")
        self.pub=self.create_publisher(String,'/chatter',10
        )


def main(args=None):
    rclpy.init(args=args)

    #code
    node=MyPublisher()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=='__main__':
    main()