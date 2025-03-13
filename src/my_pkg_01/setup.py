from setuptools import find_packages, setup

package_name = 'my_pkg_01'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aniketh05',
    maintainer_email='aniketh05@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'my_first_node = my_pkg_01.my_first_node:main',  
        'set_pen_client = my_pkg_01.set_pen_client:main',
        'pose_color_change = my_pkg_01.pose_color_change:main',
    ],
},

)
