#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''利用内建sys模块输出Hello World！
 第一行可以在linux/mac等系统中直接运行
本注释表示模块的文档注释，任何模块代码的
第一个字符串都被视为模块的文档注释；
 '''

__author__ = 'Michael Liao'#作者信息

import sys #导入模块
#sys指向该模块，该模块有argv变量，list存储
#命令行所有参数，其至少有一个元素，为该py文件名称
def test():
    args = sys.argv
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__=='__main__':#命令行运行模块文件时，
#自动将__name__属性置为__main__,
#这种if测试可以让一个模块通过命令行运行
#时执行一些额外的代码，最常见的就是运行测试。
    test()
	
#别名

try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO

try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5	
	
#作用域
print '你好'.decode("utf-8").encode("utf-8")
print sys.getdefaultencoding()
#__author__这类变量表示特殊变量，可以被直接引用__author__，__name__，__doc__（文档注释）
#_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

#第三方模块加载路径
import sys
print sys.path
#修改
sys.path.append('/Users/michael/my_py_scripts')#运行时有效
#设置环境变量PYTHONPATH，其本身的内置路径不受影响
