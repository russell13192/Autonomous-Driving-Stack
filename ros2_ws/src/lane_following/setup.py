from setuptools import setup

package_name = 'lane_following'

setup(
    name=package_name,
    version='0.0.1',
    packages=[
        'train',
    ],
    py_modules=[
        'collect',
        'drive',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='George Murray',
    author_email='russell13192@gmail.com',
    maintainer='George Murray',
    maintainer_email='russell13192@gmail.com',
    keywords=[
        'ROS',
        'ROS2',
        'deep learning',
        'lane following',
        'end to end',
        'LGSVL Simulator',
        'Autonomous Driving'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Sofware Development',
    ],
    description='ROS1/ROS2 based autonomous driving stack',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'collect = collect:main',
            'drive = drive:main',
        ],
    },
)