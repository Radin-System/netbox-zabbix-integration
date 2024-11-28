from setuptools import find_packages, setup

setup(
    name='netbox-zabbix-integration',
    version='1.0.0',
    description='A netbox plugin for zabbix integration',
    install_requires=[
        'zabbix_utils',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)