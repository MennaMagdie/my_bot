import os

from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():

        # Including the Gazebo launch file
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
             )
    
    return LaunchDescription([
        # 1. Launching robot_state_publisher for bot1
        ExecuteProcess(
            cmd=['ros2', 'run', 'robot_state_publisher', 'robot_state_publisher', '~/dev_ws/src/my_bot/description/robot_urdf1.urdf', '__ns:=/bot1'],
            output='screen',
            shell=True,
        ),
        # 2. Launching robot_state_publisher for bot2
        ExecuteProcess(
            cmd=['ros2', 'run', 'robot_state_publisher', 'robot_state_publisher', '~/dev_ws/src/my_bot/description/robot_urdf2.urdf', '__ns:=/bot2'],
            output='screen',
            shell=True,
        ),
        # 3. Launching Gazebo
        gazebo,
        # 4. Spawn entity manouna for bot1
        ExecuteProcess(
            cmd=['ros2', 'run', 'gazebo_ros', 'spawn_entity.py', '-topic', '/bot1/robot_description', '-entity', '/manouna', '__ns:=/bot1'],
            output='screen',
            shell=True,
        ),
        # 5. Spawn entity maryouma for bot2
        ExecuteProcess(
            cmd=['ros2', 'run', 'gazebo_ros', 'spawn_entity.py', '-topic', '/bot2/robot_description', '-entity', '/maryouma', '__ns:=/bot2'],
            output='screen',
            shell=True,
        ),

    ])
