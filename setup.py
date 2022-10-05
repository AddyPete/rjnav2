from setuptools import setup

package_name = 'rjnav2'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/rjnav2_launch.py']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/adeptNav2.wbt']))
data_files.append(('share/' + package_name + '/resource', ['resource/Pioneer_3-DX.urdf','resource/ros2control.yml']))
data_files.append(('share/' + package_name, ['package.xml']))
#data_files.append(('share/' + package_name + '/config', ['config/ekf.yaml']))
#data_files.append(('share/' + package_name + '/config', ['config/my_robot_lds_2d.lua','config/ekf.yaml','config/rviz_config.rviz']))
data_files.append(('share/' + package_name + '/config', ['config/ekf.yaml','config/rviz_config.rviz','config/slam_config.yaml']))
#data_files.append(('share/' + package_name + '/config', ['config/rviz_config.rviz']))
setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rjrobotics',
    maintainer_email='rjrobotics@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'adeptnav2 = rjnav2.adeptnav2:main',
            'odom_estimator = rjnav2.odom_estimator_2:main',
        ],
    },
)