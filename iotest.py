#coding: utf-8
import os
from lib2to3.fixer_util import String
#读文件
path=os.path.split(os.path.realpath(__file__))[0]+'/test.txt'
f = open(path, 'r')
print f.read()
#标示符'r'表示读

#如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：

#f=open('/Users/michael/notfound.txt', 'r')
#print f.read()

try:
    f = open('/path/to/file', 'r')
    print f.read()
except:
    pass
finally:
    if f:
        f.close()

#Python引入了with语句来自动帮我们调用close()方法：
with open(path, 'r') as f:
    print f.read()

    
    #read()一次性读取最方便；
    #如果不能确定文件大小，反复调用read(size)比较保险；
    #如果是配置文件，调用readlines()最方便：
with open(path, 'r') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉

#像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，
#还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。

#要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
imgpath=os.path.split(os.path.realpath(__file__))[0]+'/test.jpg'
f = open(imgpath, 'rb')
print f.read(10)
f.close()
#字符编码
#要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件：

f = open(path, 'r')
u = f.read().decode('gbk')
print u
f.close()
#Python还提供了一个codecs模块帮我们在读文件时自动转换编码，直接读出unicode：
import codecs
with codecs.open(path, 'r', 'utf-8') as f:
    print f.read() # u'\u6d4b\u8bd5'

#写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：

with open(path, 'w') as f:#a追加文件
    f.write('Hello, world!你好世界\n')
#要写入特定编码的文本文件，请效仿codecs的示例，写入unicode，由codecs自动转换成指定编码。
with codecs.open(path, 'a', 'gbk') as f:
    f.write('1122334455') # u'\u6d4b\u8bd5'
    
    
#操作文件目录
print "####操作文件与目录####"
import os
print os.name
#print os.uname() 查看详细信息，windows系统不提供
print os.environ #环境变量
print os.environ.get("PATH","no item!")
print os.getenv("PATH", "no item!")

# 查看当前目录的绝对路径:
abspath=os.path.abspath('.')
print abspath
# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
testdir=os.path.join(abspath, 'testdir')
print testdir
# 然后创建一个目录:
os.mkdir(testdir)
# 删掉一个目录:
os.rmdir(testdir)
print os.path.split('/Users/michael/testdir/file.txt')#拆分路径
print os.path.splitext('/Users/michael/testdir/file.txt')[1]#得到扩展名
# 对文件重命名:
os.rename('test.txt', 'test.py')
os.rename('test.py', 'test.txt')
# 删掉文件:
# os.remove('text.ttt')

import shutil
shutil.copyfile('test.txt', 'text.ppp')#利用shutil复制文件

print [x for x in os.listdir('.') if os.path.isdir(x)]#过滤文件，列出所有目录

print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']


def search(dir,word):
    ans=[]
    #先找文件
    ans+=[x for x in os.listdir(dir) if os.path.isfile(x) and word in os.path.split(x)[1]]
    ans=map(lambda x:dir+'\\'+x,ans)
    #处理目录
    for filename in os.listdir(dir):
        tmppath=os.path.join(dir,filename)#得到每个item路径
        if os.path.isdir(tmppath):
           ans+=search(tmppath,word)
    return ans

ans=search('.', 'test')
print ans

#序列化
try:
    import cPickle as pickle
except ImportError:
    import pickle
#首先，我们尝试把一个对象序列化并写入文件：

d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)
#pickle.dumps()方法把任意对象序列化成一个str，然后，就可以把这个str写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

#当我们要把对象从磁盘读到内存时，可以先把内容读到一个str，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print d

#JSON
import json
d = dict(name='Bob', age=20, score=88)
print json.dumps(d)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str)

#json化自定义对象
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
#自定义对象转化需要加参数，利用obj的dict属性，dict对象可以直接转化为json
print(json.dumps(s, default=lambda obj: obj.__dict__))
