import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/aniketh05/my_ros2_ws/src/install/my_pkg_prac'
