import rclpy
from rclpy.node import Node 
from turtlesim.srv import SetPen
from turtlesim.msg import Pose

class PenChanger(Node):
    def __init__(self):
        super().__init__('pose_color_change')
        self.subscriber=self.create_subscription(Pose, '/turtle1/pose', self.pose_callback,10)
        self.client=self.create_client(SetPen, '/turtle1/set_pen')
        
    def pose_callback(self, msg):
        if msg.y > 5.5: 
            self.change_pen_color(0, 255, 0, 5, 0)  
        else:
            self.change_pen_color(0, 0, 255, 3, 0)  

    def change_pen_color(self,r,g,b,width,offset):
        request=SetPen.Request()
        request.r, request.g, request.b = r, g, b
        request.width, request.off = width, offset
        self.client.call_async(request)

def main():
    rclpy.init()
    node=PenChanger()
    rclpy.spin(node)
    rclpy.destroy_node()
    rclypy.shutdown()

if __name__=='__main__':
    main()

