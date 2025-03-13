import rclpy
from rclpy.node import Node 
from turtlesim.srv import SetPen

class PenClient(Node):
    def __init__(self):
        super().__init__('set_pen_client')
        self.client=self.create_client(SetPen, '/turtle1/set_pen')
        self.request=SetPen.Request()
        self.call_service(255,0,0,5,0)

    def call_service(self,r,g,b,width,offset):
        self.request.r=r
        self.request.g=g
        self.request.b=b
        self.request.width=width
        self.request.off=offset
        self.future=self.client.call_async(self.request)


def main():
    rclpy.init()
    node=PenClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()

