import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
class Circular(Node):
    def __init__(self):
        super().__init__("circular_motion")
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.pose_sub = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
        self.timer = self.create_timer(0.1, self.send_vel_cmd)
        self.get_logger().info("Start moving in circle and subscribing to pose")
        self.pose = Pose()
    
    def send_vel_cmd(self):
        msg = Twist()
        
        x_min, x_max = 1.0, 10.0
        y_min, y_max = 1.0, 10.0
        
        if self.pose.x <= x_min or self.pose.x >= x_max or self.pose.y <= y_min or self.pose.y >= y_max:
            msg.linear.x = 0.4 
            msg.angular.z = 1.0 
        else:
            msg.linear.x = 1.0 
            msg.angular.z = 0.0  
        
        self.cmd_vel_pub.publish(msg)

    def pose_callback(self, msg):
        self.pose = msg
        self.get_logger().info(f"Turtle Pose - x: {msg.x:.2f}, y: {msg.y:.2f}, theta: {msg.theta:.2f}")

def main(args=None):
    rclpy.init(args=args)
    node = Circular()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()