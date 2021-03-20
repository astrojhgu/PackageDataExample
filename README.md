# PackageDataExample
## 这里展示了如何读取package自带的数据

`PackageDataExample/data/data.txt`是一个假想的数据文件

在[PackageDataExample/submod.py](PackageDataExample/submod.py)中的`read_data`函数读取了这个数据文件的内容


为了将数据文件随代码一并安装，需要修改[setup.py](setup.py)



```
python2 ./setup.py build #在实际的代码中，可以考虑将build替换为install
cd build/lib
python
>>> import PackageDataExample.submod
>>> PackageDataExample.submod.read_data() #查看PackageDataExample/submod.py中关于如何提取数据文件名的示例
```
