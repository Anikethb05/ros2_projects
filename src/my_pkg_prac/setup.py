from setuptools import find_packages, setup

package_name = 'my_pkg_prac'

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
    #tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "my_pub_node=my_pkg_prac.my_pub_node:main",
            "my_pose_sub=my_pkg_prac.my_pose_sub:main",
            "move_circular=my_pkg_prac.move_circular:main",
            "pub_sub_node=my_pkg_prac.pub_sub_node:main",
            "pen_change=my_pkg_prac.pen_change:main",
            "pub=my_pkg_prac.pub:main",
            "sub=my_pkg_prac.sub:main",
            "shape=my_pkg_prac.shape:main"
        ],
    },
)
