import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class ServiceClient(Node):

    def init(self):
        super().init('service_client')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available...')

        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        return self.cli.call_async(self.req)


def main():
    rclpy.init()
    client = ServiceClient()

    future = client.send_request(5, 7)

    rclpy.spin_until_future_complete(client, future)

    response = future.result()
    client.get_logger().info(f'Result: {response.sum}')

    client.destroy_node()
    rclpy.shutdown()


if name == 'main':
    main()