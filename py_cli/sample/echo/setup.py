#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="my_echo_cmd",
    version="0.1",
    py_modules=["my_echo"],
    include_package_ata = True,
    install_requires=["click"],
    entry_points={
        'console_scripts': [
            'my_echo = echo.main'
        ],
    },
)
