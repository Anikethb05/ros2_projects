#usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import sys

class MyClient(Node):
    def __init__(self):
        super().__init__("my_client")
        self.client=self.create_client(AddTwoInts,"add_ints")
        self.request=AddTwoInts.Request()

    def send_request(self,a,b):
        self.request.a=a
        self.request.b=b
        return self.client.call_async(self.request)

def main(args=None):
    rclpy.init(args=args)
    node=MyClient()
    future=node.send_request(int(sys.argv[1]),int(sys.argv[2]))
    rclpy.spin_until_future_complete(node,future)
    response=future.result()
    node.get_logger().info("Result of adding two numbers is: "+str(response.sum))
    rclpy.shutdown()