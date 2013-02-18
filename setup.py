#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name='haproxy-manager',
    version='0.0.1-1',
    description='A simple manager for haproxy configuration files via HTTP',
    author='Locaweb',
    url='http://github.com/locaweb/haproxy-manager',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    data_files=[
        ('/usr/sbin', ['bin/haproxy-manager']),
        ('/etc/haproxy-manager', ['etc/haproxy-manager.cfg']),
    ],
)
