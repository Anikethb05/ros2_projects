from setuptools import find_packages
from setuptools import setup

setup(
    name='my_msg_srv',
    version='0.0.0',
    packages=find_packages(
        include=('my_msg_srv', 'my_msg_srv.*')),
)
