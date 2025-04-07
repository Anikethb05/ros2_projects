cmake_minimum_required(VERSION 3.8)
project(my_gesture_arm_robot)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(gazebo_ros_pkgs REQUIRED)
find_package(xacro REQUIRED)
find_package(urdf REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(launch_ros REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# Install launch, urdf, and world files
install(DIRECTORY
  launch
  urdf
  worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
