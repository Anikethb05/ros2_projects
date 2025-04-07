#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class Add(Node):
    def __init__(self):
        super().__init__("add_two_ints")
        self.service= self.create_service(AddTwoInts,"add_ints",self.add_ints)

    def add_ints(self,request,response):
        response.sum=request.a+request.b
        return response
    
def main(args=None):
    rclpy.init(args=args)
    node=Add()
    rclpy.spin(node)
    rclpy.shutdown()
