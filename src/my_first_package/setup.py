from setuptools import find_packages, setup

package_name = 'my_first_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/multi_node_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='VaibhavDeveloper',
    maintainer_email='VaibhavDeveloper@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publisher_node = my_first_package.publisher_node:main',
            'subscriber_node = my_first_package.subscriber_node:main',
            'add_two_ints_server= my_first_package.add_two_ints_server:main',
            'add_two_ints_client= my_first_package.add_two_ints_client:main',
            'fibonacci_action_server= my_first_package.fibonacci_action_server:main',
            'parameter_example = my_first_package.parameter_example:main',
            'parameter_callback_example = my_first_package.parameter_callback_example:main'
        ],
    },
)
