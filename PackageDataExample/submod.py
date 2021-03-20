# -*- coding: utf-8 -*-
import pkg_resources #加上这个import

print(__package__) #此行无用，仅用于调试

def read_data():
    #下面这行用于提取以包目录为基准路径的具体文件的完整路径
    fname=pkg_resources.resource_filename(__package__,'data/data.txt')
    print(fname)
    #这里以读取文件内容为例示范如何使用上面得到的文件路径
    return open(fname).read()
