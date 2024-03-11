# Cleaning-Robot-Simulation
This project focuses on simulating the physical properties, geometry and perception of a cleaning robot in a virtual environment using ROS2, Gazebo and Rviz. The simulated robot is equipped with sensors such as LiDAR, depth camera, and IMU, providing a realistic representation of the robot's virtual surroundings. Additionally, a bridge between Gazebo and ROS2 environments has been implemented to facilitate seamless communication and control.

## Features
- URDF Model: URDF model defining its physical properties and geometry.
- Simulation Sensors: Implementation of sensors such as LiDAR, depth camera, and IMU to provide perception capabilities in the simulation environment.
- Gazebo-ROS2 Bridge: Implementation of a bridge between Gazebo and ROS2 environments for seamless integration and communication.
- Control: Differential drive controller to move robot.
- Command Multiplexer: Implementation of a command multiplexer to manage and prioritize commands sent to the robot's control system.


## Prerequisites
Before running the simulation, ensure you have the following installed:

ROS2 Humble or later  
Gazebo  
RViz  
Python 3.x  

## Usage
Run the launch file:
