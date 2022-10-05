import rclpy
from rclpy.time import Time
from geometry_msgs.msg import Twist, TransformStamped, Quaternion, Vector3
from sensor_msgs.msg import LaserScan, Imu
from geometry_msgs.msg import TransformStamped
from tf2_ros import StaticTransformBroadcaster, TransformListener, Buffer, TransformBroadcaster
from nav_msgs.msg import Odometry
import numpy as np
import tf_transformations
from math import sqrt

HALF_WIDTH = (497/1000)/2
HALF_LENGTH = HALF_WIDTH
ROBOT_ROTATION_RADIUS = sqrt(HALF_LENGTH ** 2 + HALF_WIDTH ** 2)
WHEEL_RADIUS = 0.11
MAX_VELOCITY = 6.4

class MyRobotDriver:
        def init(self, webots_node, properties):
            self.__robot = webots_node.robot
            
            self.__front_left_motor = self.__robot.getDevice('left wheel')
            self.__front_right_motor = self.__robot.getDevice('right wheel')

            self.__front_left_motor.setPosition(float('inf'))
            self.__front_left_motor.setVelocity(0)

            self.__front_right_motor.setPosition(float('inf'))
            self.__front_right_motor.setVelocity(0)

            self.__target_twist = Twist()
            
            rclpy.init(args=None)
            self.__node = rclpy.create_node('adeptnav2')
            self.__node.create_subscription(Twist, 'cmd_vel', self.__cmd_vel_callback, 1)

        def __cmd_vel_callback(self, twist):
            self.__target_twist = twist

        def step(self):
            rclpy.spin_once(self.__node, timeout_sec=0)

            forward_speed = self.__target_twist.linear.x
            angular_speed = self.__target_twist.angular.z

            command_motor_left = (forward_speed - angular_speed * ROBOT_ROTATION_RADIUS) / WHEEL_RADIUS
            command_motor_left = min(command_motor_left, MAX_VELOCITY)
            command_motor_right = (forward_speed + angular_speed * ROBOT_ROTATION_RADIUS) / WHEEL_RADIUS
            command_motor_right = min(command_motor_right, MAX_VELOCITY)

            self.__front_left_motor.setVelocity(command_motor_left)
            self.__front_right_motor.setVelocity(command_motor_right)