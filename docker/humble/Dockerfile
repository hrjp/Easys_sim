ARG BASE_IMAGE=hrjp/ros2:humble_cuda
FROM $BASE_IMAGE

RUN cd /home/colcon_ws/src && \
    git clone https://github.com/hrjp/Easys_sim && \
    git clone https://github.com/hrjp/Easys_ros && \
    ./Easys_sim/package_install.bash && \
    cd .. && \
    pip install setuptools==58.2.0 && \
    colcon build --symlink-install && \
    source install/setup.sh && \
    apt clean
WORKDIR /home/catkin_ws