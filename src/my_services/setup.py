from setuptools import find_packages, setup

package_name = 'my_services'

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
    maintainer_email='anikethbhargav05@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "add_two_ints=my_services.add_two_ints:main",
            "my_client=my_services.my_client:main"
        ],
    },
)
