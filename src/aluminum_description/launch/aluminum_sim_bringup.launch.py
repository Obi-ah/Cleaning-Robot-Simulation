import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node, SetParameter
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import xacro

def generate_launch_description():
    ld = LaunchDescription()

    pkg_name = 'aluminum_description'


    # urdf
    xacro_file = os.path.join(get_package_share_directory(pkg_name),'urdf', 'aluminum.xacro.urdf')

    robot_description_raw = xacro.process_file(xacro_file).toxml()

    # robot state publisher
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw}] 
    )

    # coursework 2
    launch_gz_rviz = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([get_package_share_directory('coursework2'), '/launch', '/sim_bringup.launch.py'])
    )

    # spawner
    node_spawn_robot = Node(package='ros_gz_sim', executable='create',
                        arguments=['-topic', '/robot_description',
                                   '-z', '0.5'],
                        output='screen')
    
    # bridge
    bridge_config = os.path.join(get_package_share_directory(pkg_name), 'config', 'bridge.yaml')

    node_ros_gz_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters= [{
                    'config_file': bridge_config},],

        output='screen'
        )

    # twist multiplexer
    twist_mux_config = os.path.join(get_package_share_directory(pkg_name), 'config', 'twist_mux.yaml')
    
    node_twist_mux = Node(
            package='twist_mux',
            executable='twist_mux',
            output='screen',
            remappings={('/cmd_vel_out', '/aluminum/cmd_vel')},
            parameters=[
                {'use_sim_time': 'True'},
                twist_mux_config,
                ]
        )

    ld.add_action(node_robot_state_publisher)
    ld.add_action(launch_gz_rviz)
    ld.add_action(node_spawn_robot)
    ld.add_action(node_ros_gz_bridge)
    ld.add_action(node_twist_mux)

    return ld