# Easys_sim
Simple simulator for underwater robot [Easys](https://github.com/tamago117/Easys_ros)

# Setup
```bash
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-nightly `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-nightly.list'
wget https://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt update
sudo apt install -y gz-garden
cd colcon_ws/src
git clone https://github.com/hrjp/Easys_sim
git clone https://github.com/osrf/lrauv.git
cd ..
colcon build --symlink-install
```