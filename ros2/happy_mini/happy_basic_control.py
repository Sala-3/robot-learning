import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class HappyBasicControl(Node):

    def __init__(self):
        super().__init__('happy_basic_control')

        # 速度指令を送るPublisher
        self.pub = self.create_publisher(
            Twist, '/cmd_vel', 10
        )

        # 0.1秒ごとに実行
        self.timer = self.create_timer(
            0.1, self.timer_callback
        )

        self.start_time = time.monotonic()
        self.done = False

        self.get_logger().info('Happy Mini control start!')

    def timer_callback(self):

        elapsed = time.monotonic() - self.start_time

        msg = Twist()

        # 0～2秒：前進
        if elapsed < 2.0:
            msg.linear.x = 0.10
            msg.angular.z = 0.0

        # 2～3秒：停止
        elif elapsed < 3.0:
            pass

        # 3～5秒：左旋回
        elif elapsed < 5.0:
            msg.linear.x = 0.0
            msg.angular.z = 0.25

        # 5～7秒：停止
        elif elapsed < 7.0:
            pass

        # 終了
        else:
            self.done = True
            self.get_logger().info('Movement finished!')

        # 速度指令を送信
        self.pub.publish(msg)


def main():

    rclpy.init()

    node = HappyBasicControl()

    try:
        while rclpy.ok() and not node.done:
            rclpy.spin_once(node, timeout_sec=0.1)

    except KeyboardInterrupt:
        pass

    finally:
        # 最後に必ず停止指令を送る
        node.pub.publish(Twist())
        time.sleep(0.2)

        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
