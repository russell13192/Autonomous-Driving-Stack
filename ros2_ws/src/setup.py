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
)