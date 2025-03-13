#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class PubSub(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.get_logger().info("Turtle Controller has been started")
        self.subscriber=self.create_subscription(Pose,"/turtle1/pose",self.sub_callback,10)
        self.publisher=self.create_publisher(Twist,"/turtle1/cmd_vel",10)

    def sub_callback(self, msg: Pose):
        cmd=Twist()
        if msg.x>=10 or msg.y>=10 or msg.x<=1 or msg.y<=1:
            cmd.angular.z=0.9
            cmd.linear.x=1.0
        else:
            cmd.linear.x=5.0
            cmd.angular.z=0.0
        self.publisher.publish(cmd)
    




def main(args=None):
    rclpy.init(args=args)
    node=PubSub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()