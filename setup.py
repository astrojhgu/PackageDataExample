#!/usr/bin/env python
from setuptools import setup

setup(
    name="TestPkg",
    author="Jhgu",
    author_email="jhgu@nao.cas.cn",
    version="0.1.0",
    packages=["TestPkg"],
    zip_safe=True,
    #加上下面这个参数，data/*.txt根据实际情况修改
    package_data={
        "":["data/*.txt"]
    },
)

