# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Twist

# class TurtlePublisher(Node):
#     def __init__(self):
#         super().__init__('turtle_publisher')
#         self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
#         self.timer = self.create_timer(0.5, self.publish_cmd)

#     def publish_cmd(self):
#         twist = Twist()
#         twist.linear.x = 2.0  # Forward velocity
#         twist.angular.z = 1.0  # Angular velocity to move in a circle
#         self.publisher.publish(twist)
#         self.get_logger().info('Publishing: Moving in a circle')

# def main(args=None):
#     rclpy.init(args=args)
#     node = TurtlePublisher()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()


# publisher_node.py
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtlePublisher(Node):
    def __init__(self):
        super().__init__('turtle_publisher')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.publish_cmd)

    def publish_cmd(self):
        twist = Twist()
        twist.linear.x = 2.0  # Move forward at constant speed
        twist.angular.z = 0.0  # No rotation (straight line)
        self.publisher.publish(twist)
        self.get_logger().info('Publishing: Moving in straight line')

def main(args=None):
    rclpy.init(args=args)
    node = TurtlePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()