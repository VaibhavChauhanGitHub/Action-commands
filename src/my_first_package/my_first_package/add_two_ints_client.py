import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__('add_two_ints_client')
        self.cli = self.create_client(AddTwoInts,'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not available waiting again")

        self.req=AddTwoInts.Request()
        self.req.a=7
        self.req.b=3

        self.future = self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)
    node= AddTwoIntsClient()
    rclpy.spin_until_future_complete(node, node.future)

    response= node.future.result()

    if response is not None:
        node.get_logger().info(f"Result of {node.req.a} + {node.req.b} = {response.sum}")
    else:
        node.get_logger().error('Service call failed')

    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()