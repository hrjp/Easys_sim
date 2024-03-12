# Easys_sim
Simple simulator for underwater robot [Easys](https://github.com/tamago117/Easys_ros)

# Setup
```bash
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt update
sudo apt install -y libgz-sim7-dev ros-humble-ros-gzgarden
cd colcon_ws/src
git clone https://github.com/hrjp/Easys_sim
cd ..
colcon build --symlink-install
```