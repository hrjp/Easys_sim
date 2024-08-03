from setuptools import find_packages, setup

package_name = 'uw_robocon_sim'
#submodule_name = package_name + '/controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hrjp',
    maintainer_email='hrjp00@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'balloon_detect = uw_robocon_sim.balloon_detect:main',
        ],
    },
)