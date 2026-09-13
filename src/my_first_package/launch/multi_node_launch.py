from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import GroupAction
from launch.conditions import IfCondition


def generate_launch_description():
    robot_speed_arg = DeclareLaunchArgument(
        name='robot_speed',
        default_value='2.0',
        description='Initial Speed of the robot'
    )
    robot_speed = LaunchConfiguration('robot_speed')
    enable_callback_arg = DeclareLaunchArgument(
        name='enable_callback',
        default_value='true',
        description='Enable callback functionality'
    )
    
    enable_callback = LaunchConfiguration('enable_callback')

    use_sim_time_arg = DeclareLaunchArgument(
        name='use_sim_time',
        default_value='false',
        description='Use simulation time of the robot'
    )
    use_sim_time = LaunchConfiguration('use_sim_time')

    return LaunchDescription([
        robot_speed_arg,
        enable_callback_arg,
        use_sim_time_arg,
        GroupAction([
            Node(
                package='my_first_package',
                executable='parameter_example',
                namespace='robot1',
                parameters=[{'robot_speed': robot_speed,'use_sim_time': use_sim_time}],
                name='parameter_node',
                output='screen'
            ),
            Node(
                package='my_first_package',
                executable='parameter_callback_example',
                namespace='robot1',
                name='callback_node',
                condition=IfCondition(enable_callback),
                parameters=[{'robot_speed': robot_speed,'use_sim_time': use_sim_time}],
                output='screen'
            )
        ])
    ])


