# import rclpy
# from rclpy.node import Node
# from turtlesim.msg import Pose

# class TurtleSubscriber(Node):
#     def __init__(self):
#         super().__init__('turtle_subscriber')
#         self.subscription = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)

#     def pose_callback(self, msg):
#         self.get_logger().info(f'Turtle Position -> X: {msg.x:.2f}, Y: {msg.y:.2f}, Theta: {msg.theta:.2f}')

# def main(args=None):
#     rclpy.init(args=args)
#     node = TurtleSubscriber()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()


# subscriber_node.py
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class TurtleSubscriber(Node):
    def __init__(self):
        super().__init__('turtle_subscriber')
        self.subscription = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.min_x, self.max_x = 0.5, 10.5
        self.min_y, self.max_y = 0.5, 10.5
        self.avoiding_wall = False
        self.turning_steps = 0
        self.max_turning_steps = 10

    def pose_callback(self, msg):
        near_left_wall = msg.x <= self.min_x
        near_right_wall = msg.x >= self.max_x
        near_bottom_wall = msg.y <= self.min_y
        near_top_wall = msg.y >= self.max_y
        near_wall = near_left_wall or near_right_wall or near_bottom_wall or near_top_wall
        
        twist = Twist()
        
        if near_wall or self.avoiding_wall:
            if near_wall and not self.avoiding_wall:
                self.avoiding_wall = True
                self.turning_steps = 0
                wall_name = "left" if near_left_wall else "right" if near_right_wall else "bottom" if near_bottom_wall else "top"
                self.get_logger().info(f'Near {wall_name} wall at X: {msg.x:.2f}, Y: {msg.y:.2f}, turning around')
            
            if self.turning_steps < self.max_turning_steps:
                twist.linear.x = 0.0
                twist.angular.z = math.pi 
                self.turning_steps += 1
            else:
                self.avoiding_wall = False
                twist.linear.x = 2.0
                twist.angular.z = 0.0
                self.get_logger().info('Completed turn, resuming straight motion')
            
            self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()