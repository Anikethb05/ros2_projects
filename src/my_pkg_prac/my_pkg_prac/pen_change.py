#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen

class PenChanger(Node):
    def __init__(self):
        super().__init__("pen_change")
        self.subscriber=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
        self.publisher=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.client=self.create_client(SetPen,"/turtle1/set_pen")
        while not self.client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service...")
        self.request=SetPen.Request()

    def pose_callback(self, msg: Pose):
        cmd=Twist()
        if msg.x>10 or msg.y>10 or msg.x<1 or msg.y<1:
            cmd.angular.z=0.9
            cmd.linear.x=1.0
        else:
            cmd.linear.x=1.0
        
        self.publisher.publish(cmd)

        if msg.x>=5.5:
            self.call_service(255,0,0,3,0)
        else:
            self.call_service(0,225,0,5,0)
        
    def call_service(self,r,g,b,w,o):
        self.request.r=r
        self.request.g=g
        self.request.b=b
        self.request.width=w
        self.request.off=o

        self.future=self.client.call_async(self.request)
        

def main(args=None):
    rclpy.init(args=args)
    node=PenChanger()
    rclpy.spin_until_future_complete(node,node.future)
    rclpy.shutdown()

# #usr/bin/env python3

# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Twist
# from turtlesim.msg import Pose
# from turtlesim.srv import SetPen
# from functools import partial


# class PenChanger(Node):
#     def __init__(self):
#         super().__init__("pen_change")
#         self.subscriber=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
#         self.publisher=self.create_publisher(Twist,"turtle1/cmd_vel",10)


#     def pose_callback(self, msg: Pose):
#         cmd=Twist()
#         if msg.x>=10 or msg.y>=10 or msg.x<=1 or msg.y<=1:
#             cmd.angular.z=0.9
#             cmd.linear.x=1.0
#         else:
#             cmd.linear.x=1.0
#         self.publisher.publish(cmd)
            
#         if msg.x>=5.5:
#             self.set_pen(255,0,0,3,0)
#         else:
#             self.set_pen(0,255,0,3,0)

#     def set_pen(self,r,g,b,width,off):
#         client=self.create_client(SetPen,"/turtle1/set_pen")
#         # while not client.wait_for_service(1.0):
#         #     self.get_logger().warn("Waiting for service...")
#         request=SetPen.Request()
#         request.r=r
#         request.g=g
#         request.b=b
#         request.width=width
#         request.off=off

#         future= client.call_async(request)
#     #     future.add_done_callback(partial(self.callback_set_pen))

#     # def callback_set_pen(self,future):
#     #     try:
#     #         response=future.result()
#     #     except Exception as e:
#     #         self.get_logger().error("Service call failed: %r" % (e,))
        

# def main(args=None):
#     rclpy.init(args=args)
#     node=PenChanger()
#     rclpy.spin(node)
#     rclpy.shutdown()

# if __name__=='__main__':
#     main()