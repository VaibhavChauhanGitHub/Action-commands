import rclpy
from rclpy.node import Node
import time

class ExecutionDemoNode(Node):
    def __init__(self):
        super().__init__('execution_demo')
        self.get_logger().info('Execution Demo Node has been started.')
        self.timer1 = self.create_timer(1.0, self.timer1_callback)
        self.timer2 = self.create_timer(1.0, self.timer2_callback)

    def timer1_callback(self):
        self.get_logger().info('Timer 1 callback executed.')
        time.sleep(2.0)
        self.get_logger().info('Timer 1 callback finished.')

    def timer2_callback(self):
        self.get_logger().info('Timer 2 callback fired.')

def main(args=None):
    rclpy.init(args=args)
    execution_demo_node = ExecutionDemoNode()
    rclpy.spin(execution_demo_node)
    execution_demo_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
        