cmake_minimum_required(VERSION 3.8)
project(Easys_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake_auto REQUIRED)

ament_auto_find_build_dependencies()

# ament_auto_add_library(Easys_description SHARED
# )

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# # Exports
# install(
#   EXPORT ${PROJECT_NAME}
#   FILE ${PROJECT_NAME}-targets.cmake
#   NAMESPACE ${PROJECT_NAME}::
#   DESTINATION share/${PROJECT_NAME}/cmake)

# include(CMakePackageConfigHelpers)
# configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/cmake/Config.cmake.in
#   "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
#   INSTALL_DESTINATION "share/${PROJECT_NAME}/cmake"
#   NO_SET_AND_CHECK_MACRO
#   NO_CHECK_REQUIRED_COMPONENTS_MACRO)
# install(FILES
#   ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake
#   DESTINATION share/${PROJECT_NAME}/cmake)

# Hooks
configure_file(
  "hooks/hook.dsv.in"
  "${CMAKE_CURRENT_BINARY_DIR}/hooks/hook.dsv" @ONLY
)
configure_file(
  "hooks/hook.sh.in"
  "${CMAKE_CURRENT_BINARY_DIR}/hooks/hook.sh" @ONLY
)




install(
  DIRECTORY 
    model 
    launch 
    config
    ${CMAKE_CURRENT_BINARY_DIR}/hooks
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
# .sdf files are installed in ~/.gazebo/models
# https://gazebosim.org/api/sim/7/resources.html
# set(HOME_DIRECTORY $ENV{HOME})
# install(
#   DIRECTORY model/
#   DESTINATION ${HOME_DIRECTORY}/.gz/fuel
#   DESTINATION ${HOME_DIRECTORY}/.ignition/fuel
#   FILES_MATCHING PATTERN "*"
# )