#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class PubSubNode(Node):
    def __init__(self):
        super().__init__("my_pose_sub")
        self.subscriber=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)

    def pose_callback(self, msg: Pose):
        self.get_logger().info(str(msg))

def main():
    rclpy.init()
    node=PubSubNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()
    