import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy

class QoSTestNode(Node):
    def __init__(self):
        super().__init__('qos_publisher')
        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10
        )
        self.publisher_ = self.create_publisher(String, 'qos_topic', qos_profile)
        self.timer = self.create_timer(1.0, self.publish_message)
        self.count = 0

    def publish_message(self):
        msg = String()
        msg.data = 'Hello, this is a QoS test message!'
        self.publisher_.publish(msg)
        self.count += 1
        self.get_logger().info('Published message: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    qos_test_node = QoSTestNode()
    rclpy.spin(qos_test_node)
    qos_test_node.destroy_node()
    rclpy.shutdown()    


if __name__ == '__main__':
    main()  