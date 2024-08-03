# Easys_sim
Simple simulator for underwater robot [Easys](https://github.com/tamago117/Easys_ros)

## Environment
* Ubuntu 22.04
* ROS2 Humble
* Gazebo Garden

## Setup

### Manual setup
```bash
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt update
sudo apt install -y libgz-sim7-dev ros-humble-ros-gzgarden
cd colcon_ws/src
git clone https://github.com/hrjp/Easys_sim
git clone https://github.com/hrjp/Easys_ros
cd ..
colcon build --symlink-install
source install/setup.sh
```

### Use docker
Setup container
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/hrjp/Easys_sim/main/docker/humble/run.bash)" -w
```
On second startup
```bash
./easys_sim.bash
```

## Usage
### joy control
```bash
ros2 launch Easys_description sim.launch.xml
```

### Under Water Robocon
```bash
ros2 launch uw_robocon_sim joy_sim.launch.xml
```

## Demo video

### Joy control
https://github.com/hrjp/Easys_sim/assets/36100321/9964a63f-17b5-44a7-9ccb-4f608dd963a4

### Under Water Robocon
https://github.com/user-attachments/assets/7f006607-5357-4538-9b65-9edd38f892ea

