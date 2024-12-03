from launch import LaunchDescription
from launch ros.actions import Node

def generate launch description():
    return LaunchDescription([
        Node(
            package='demo_nodes_py',
            executable='listener'
        )
    ])