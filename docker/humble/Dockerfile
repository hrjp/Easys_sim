ARG BASE_IMAGE=hrjp/ros2:humble_cuda
FROM $BASE_IMAGE

RUN cd /home/colcon_ws/src && \
    git clone https://github.com/hrjp/Easys_sim && \
    git clone https://github.com/hrjp/Easys_ros && \
    ./Easys_sim/package_install.bash && \
    cd .. && \
    rosdep update && \
    rosdep install --from-paths src -y --ignore-src  &&\
    /bin/bash -c "source /opt/ros/humble/setup.bash; colcon build --symlink-install" && \
    apt clean
WORKDIR /home/catkin_ws