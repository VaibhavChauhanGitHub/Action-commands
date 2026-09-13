from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import os 
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    pkg_share = get_package_share_directory('integration_demo')
    param_file = os.path.join(pkg_share, 'config', 'params.yaml')
    robot_speed_arg = DeclareLaunchArgument(
        name='robot_speed',
        default_value='2.0',
        description='Initial Speed of the robot'
    )
    robot_speed = LaunchConfiguration('robot_speed')


    return LaunchDescription([
        robot_speed_arg,
        Node(
            package='integration_demo',
            executable='velocity_publisher',
            namespace='robot1',
            parameters=[param_file],
            name='velocity_publisher',
            output='screen'
        )
    ])