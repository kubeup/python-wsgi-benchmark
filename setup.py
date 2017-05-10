#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name="python-wsgi-benchmark",
    version="0.1",
    license='BSD',
    description="Benchmark Python WSGI servers and frameworks",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'gevent_server=server.gevent_server:main',
            'meinheld_server=server.meinheld_server:main',
            'bjoern_server=server.bjoern_server:main',
        ],
    },
)
