# PackageDataExample
```
python2 ./setup.py build #在实际的代码中，可以考虑将build替换为install
cd build/lib
python
>>> import PackageDataExample.submod
>>> PackageDataExample.submod.read_data() #查看PackageDataExample/submod.py中关于如何提取数据文件名的示例
```
