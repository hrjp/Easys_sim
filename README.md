# Easys_sim
Simple simulator for underwater robot [Easys](https://github.com/tamago117/Easys_ros)

## Environment
* Ubuntu 22.04
* ROS2 Humble
* Gazebo Garden

## Setup
```bash
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt update
sudo apt install -y libgz-sim7-dev ros-humble-ros-gzgarden
cd colcon_ws/src
git clone https://github.com/hrjp/Easys_sim
git clone https://github.com/tamago117/Easys_ros
cd ..
colcon build --symlink-install
source install/setup.sh
```

## Usage
```bash
ros2 launch Easys_description sim.launch.xml
```

## Demo video
https://github.com/hrjp/Easys_sim/assets/36100321/9964a63f-17b5-44a7-9ccb-4f608dd963a4

