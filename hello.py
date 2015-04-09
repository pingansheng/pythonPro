#coding: gbk

print 'hello world'
print 'The quick brown fox',    'jumps over', 'the lazy dog'
name=raw_input('please enter your name:')
print 'hello',name


print '\\\t\\'
print r'\\\t\\' #表示不进行转义
print 'I\'m \"OK\"'


print '''line1
line2
line3'''  #表示多行内容，省去写\n

print len('中文')
print len(u'中文')

#格式化输出字符串
print 'Hi, %s, you have $%d.' % ('Michael', 1000000)
print '%2d-%03d' % (3, 1)
print '%.2f' % 3.1415926

#LIST
classmates = ['Michael', 'Bob', 'Tracy']
classmates.sort() #排序
print len(classmates)
print classmates[0]
print classmates[-1] #直接获取最后一个元素，以此类推，可以获取倒数第2个[-2]、倒数第3个[-3]
classmates.append('Adam')
classmates.insert(1,'Jack')
classmates.pop() #删除最后一个元素
classmates.pop(1) #删除第i+1个元素

print classmates

#tuple 一旦定义不可改变

classmates = ('Michael', 'Bob', 'Tracy')

t=(1,) #一个元素的tuple定义方式，消除小括号歧义
#一种可变的tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t



#条件
age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'

birth = int(raw_input('birth: ')) #raw_input()返回永远是string
if birth < 2000:
    print '00前'
else:
    print '00后'

#循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

sum = 0
for x in range(101):  #range(m)生成0-(m-1)的序列
    sum = sum + x
print sum

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

#DICT hash_map

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']
d['Adam'] = 67

#判断是否存在key
print 'Thomas' in d
if 'Thomas' in d:
    print d['Thomas']
if d.get('Thomas') != None:
    print d['Thomas']
else:
    print None
#key必须是不可变对象,字符串，整数等均是，不可变对象操作后不改变自身

#SET 无序无重复
s = set([1, 2, 3])
s = set([1, 1, 2, 2, 3, 3])
s.add(4)
s.remove(4)

s1=set([1,2,3])
s2=set([1,2,4])
print s1 & s2 #并集
print s1 | s2 #交集


#函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

#空函数
def nop():
    pass
#pass的另一个用途
if age >= 18:
    pass

#加入参数检查的函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#多个返回值的函数，本质上返回的是tuple！
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

#函数默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

enroll('Adam', 'M', city='Tianjin') #调用时可以指定某个固定参数


def add_end(L=None): #默认参数必须指向不可变对象，否则每次调用函数，默认参数的值均会改变
    if L is None:
        L = []
    L.append('END')
    return L

#函数可变参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1,2,3)

nums = [1, 2, 3]
calc(*nums) #将List或者triple变为可变参数

#关键字参数,允许你传入0个或任意个含参数名的参数(用于封装dict)

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
#关键字参数在函数内部自动组装为一个dict

person('Bob', 35, city='Beijing')
#name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer')
#name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

#可以组合dict调用
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)
#name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
#name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

#函数参数组合，多种函数类型同时使用

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1, 2)
#a = 1 b = 2 c = 0 args = () kw = {}
func(1, 2, c=3)
#a = 1 b = 2 c = 3 args = () kw = {}
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b',99)
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
func(1, 2, 3, 'a', 'b', x=99)
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}

#可以神奇大使用triple和dict调用
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)
#a = 1 b = 2 c = 3 args = (4,) kw = {'x': 99}
#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

##函数部分小结
#Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#默认参数一定要用不可变对象，如果是可变对象，运行会有逻辑错误！
#要注意定义可变参数和关键字参数的语法：
#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。
#以及调用函数时如何传入可变参数和关键字参数的语法：
#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#尾递归，return只返回函数

#切片操作 [开始:结束:步长]
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L[0:3] #从索引0开始，取前三个
print L[:3] #索引为0可忽略
print L[1:3] #从索引1开始，取前三个
print L[-2:] #从倒数第二个开始，直到最后
print L[-2:-1] #从倒数第二个开始，直到最后的前一个
L = range(100)
print L[:10] #前10个数
print L[-10:] #后10个数
print L[10:20] #第11个数到第20个
print L[:10:2] #前10个，每隔2个取一个
print L[::5] #每隔5个取一个
print L[:] #输出整个数组

#triple，字符串等均可使用切片
print (0, 1, 2, 3, 4, 5)[:3]
print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]

#迭代
d = {'a': 1, 'b': 2, 'c': 3}

print "迭代Dict的Key"
for key in d:
     print key

print "迭代Dict的Value"
for value in d.itervalues():
     print value

print "同时迭代Dict的Key与Value"
for key,value in d.iteritems():
     print key,value

print "迭代字符串"
for ch in 'ABC':
     print ch
#判断一个对象是否可迭代
from collections import Iterable
print isinstance('abc', Iterable) # str是否可迭代
#True
print isinstance([1,2,3], Iterable) # list是否可迭代
#True
print isinstance(123, Iterable) # 整数是否可迭代
#False

#Python内置的enumerate函数可以把一个
#list变成索引-元素对，这样就可以在for循环
#中同时迭代索引和元素本身：

list=['A','B','C']
for i, value in enumerate(list):
    print i, value

#列表生成式
print range(1, 11)

print [x * x for x in range(1, 11)]

print [x * x for x in range(1, 11) if x % 2 == 0] #加入条件判断

print [m + n for m in 'ABC' for n in 'XYZ'] #两层循环生成全排列

#示例，列出目录所有文件
import os # 导入os模块
print [d for d in os.listdir('C:\\')] # os.listdir可以列出文件和目录

#for循环可以使用多个变量
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.iteritems():
    print k, '=', v

#列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k + '=' + v for k, v in d.iteritems()]

#list所有字符串变小写
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]
#isinstance可用于判断数据的类型与具体情况，如判断字符串isinstance(a,str)
print isinstance(12.1,int)

#生成器generator，可以使用时推算出后面的元素，节省空间
L = [x * x for x in range(10)]
g = (x * x for x in range(10)) #列表生成器变为()就是创建generator
#generator.next()方法可以得到元素，一般使用for循环迭代
for n in g:
    print n
#第二中创建方式，函数中使用yield关键字
#斐波那契数列函数，generator的函数每次调用next()的时候执行，遇到yield语句返回，
#再次执行时从上次返回的yield语句处继续执行。一般使用for循环执行
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for i in fib(10):
    print i

#函数式编程
#变量可以指向函数
f=abs
print f(-5)

#map/reduce函数

#map()函数接收两个参数，一个是函数，一个是序列，
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。

def f(x):
    return x**2

a=map(f,[1,2,3,4,5,6,7,8,9])
print a;

def check(s):
    return s[0].upper()+s[1:].lower()
name=['adam', 'LISA', 'barT']
print map(check,name)

#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数
#reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def add(x, y):
    return x + y

print reduce(add, [1, 3, 5, 7, 9]) #((((1+3)+5)+7)+9)

#利用reduce求积
def prod(A=[]):
    return reduce(lambda x,y:x*y,A)
print prod([1,2,3,4,5,6,7,8,9,10])

#组合使用
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
   '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def fn(x, y):
    return x * 10 + y
print reduce(fn, map(char2num, '13579'))
#字符串转换整数，map(char2num, '13579')=[1,3,5,7,9]

#filter函数，过滤序列
def is_odd(n):
    return n % 2 == 1

print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])

#sorted函数

print sorted([6,5,4,3,2,1])


#可以传入函数进行比较
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
	
print sorted([36, 5, 12, 9, 21], reversed_cmp)

#忽略大小写的字符串排序函数
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)	
		
#函数作为返回值
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print f()
#内部函数sum引用外部函数lazy_sum的参数和局部变量
#lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中,称为“闭包”

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1(),f2(),f3()#9,9,9
#返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，i已经变成了3，因此最终结果为9。
#使用闭包时候：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#解决方案:添加函数用参数绑定(函数参数绑定后不改变)，可使用lambda函数缩短代码

#匿名函数，lambda表示匿名函数
map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
f = lambda x: x * x#可以赋值
def build(x, y):
    return lambda: x * x + y * y#可以返回
	
#装饰器	
#函数是一个对象，函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print '2013-12-25'
f = now
f()#2013-12-25
print now.__name__#函数有name属性
print f.__name__
#增强now()函数的功能，在函数调用前后自动打印日志，不希望修改now()函数的定义
#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log#使用@放置装饰器
def now():
    print '2013-12-25'
now()#now = log(now)

#需要参数的装饰器
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print '2013-12-25'

now()#now = log('execute')(now)

#使用装饰器后函数name属性变化，使用funtools修正，一个完整的装饰器如下
#@functools.wraps(func)置于wrapper定义之前

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
	
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print '2013-12-25'

print now.__name__#now

#两种方式自适应前后打印日志
def log(text_fun):#此参数为指定的文本或者函数名
    if isinstance(text_fun,str):
        def decorator(func):#若text_fun为文本，则func为第二个函数名参数
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print 'before',"".join(text_fun)
                func(*args, **kw)
                print 'after',"".join(text_fun)
            return wrapper
        return decorator
    else:#此处调用需与text_fun一致
        @functools.wraps(text_fun)
        def wrapper(*args, **kw):
            print 'before'
            text_fun(*args, **kw)
            print 'after'
        return wrapper
    
@log
def now():
    print '2013-12-25'

now()

@log('111')
def now():
    print '2013-12-25'

now()


#偏函数，利用functools
print int('123',base=8)#以8进制进行转换
#利用偏函数简化
int2 = functools.partial(int, base=2)
print int2('10101010')


#模块，见moudle.py

#面向对象

class Student(object):#括号内表示继承

    def __init__(self, name, score):#构造函数，首个参数为self
        self.name = name
        self.__score = score#私有变量，但是仍可以通过xx._Student_name访问，不建议
							#单下划线_name变量表示不建议直接访问，虽然可以

    def print_score(self):
        print '%s: %s' % (self.name, self.score)



class Animal(object):

    def run(self):
        print "Animal is running"

class Dog(Animal):

    def run(self):
        print "Dog is running"
a=Animal()
a.run()

d=Dog()
d.run()

#获取类型信息
print type(a)

print type(a)==type(d)

import types

print type(Animal)==types.TypeType
#type(int)==type(str)==types.TypeType True类型本身的类型是TypeType

#isinstance
print isinstance(d,Animal)

print isinstance(12,(int,str,Animal))#判断12是不是其中一种

#dir()打印对象所有属性与方法,包括内置属性
print dir('ABC')

#得到对象属性状态
if hasattr(d,'age'):
    print d.age
else:
    setattr(d,'age',19)
    print d.age 

print getattr(d,'z','null')#获取属性'z'，如果不存在，返回默认值null

#获得方法
fn=getattr(d,'run')
fn()

#面向对象高级

d.name = 'Michael' # 动态给实例绑定一个属性

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
d.set_age = MethodType(set_age,d, Dog) # 给实例绑定一个方法,对其他实例不起作用
d.set_age(20)
print d.age

Dog.set_age = MethodType(set_age, None, Dog) # 对类绑定，所有实例起作用

# __slots__变量可以限制类可以后期添加的属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
s=Student()
s.age=15
#出错 s.score=20

#子类不起作用，除非在子类中也定义__slots__，子类允许定义的属性就是自身的__slots__加上父类的__slots__


class Student(object):

    @property #把一个方法变成属性调用
    def score(self):
        return self._score

    @score.setter #setter变为属性赋值
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s=Student()
s.score=100
print s.score

#s.score=200 出错

#多重继承

class Flyable(object):
    def fly(self):
        print('Flying...')

class Bird(Animal,Flyable):
    pass
    
B=Bird()
B.fly()
#一般这种功能称为Mixin，常改为 FlyableMixin

#定制类，实现类似Java toString()等方法
#__len__()<=>len()
#__str__()<=>print ...
#__repr__(),使用对象名调用，返回调试信息，一般  __repr__ = __str__
#__iter__用于 for in迭代
#__getitem__下标取元素
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

    def __getitem__(self, n):
        if isinstance(n, int):#下标
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):#切片类型
            start = n.start
            stop = n.stop
            step=n.step
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            L=L[::step]#处理step
            return L
F=Fib()
for n in F:
    print n
    
print F[5]
print F[0:5]
print F[0:5:2]

#__getattr__  调用不存在的属性时，Python解释器会试图调用__getattr__(self, 'XXX')来尝试获得属性

class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
S=Student()
print S.age()
#print S.pp

#链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __repr__(self):
        return self._path
    
    def __call__(self, *args,**dict):
        for arg in args:
            self._path+='('+str(arg)+')'
        for key in dict:
            self._path+='('+str(key)+'='+str(dict[key])+')'
        return Chain(self._path)

c=Chain()
#c.status调用__getattr__返回一个对象实例，所以可以调用__call__()
print c.status('良好',statuscode=200).timeline.list('pingansheng')

#__call__直接对实例进行调用
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
        
s = Student('Michael')
s()
#Callable可判断对象是否为函数或带有__call()__的实例
print callable(s)

#动态语言当中，函数与类的定义是在运行时创建的
#创建的方法就是type(),可以用type()方法创建一个类
def fn(self,name='world'):
    print('Hello ,%s'  % name)
Hello=type('Hello',(object,),dict(hello=fn)) #(类名称，父类triple，方法名称与函数的绑定)
h=Hello()
h.hello()
print type(Hello)
print type(h)

#metaclass，用于创造与动态改变类本身，略过


#错误、调试和测试

try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else: #未捕获到异常执行
    print 'no error!'
finally:
    print 'finally...'
print 'END'
#异常继承树
"""
        BaseException
         +-- SystemExit
         +-- KeyboardInterrupt
         +-- GeneratorExit
         +-- Exception
              +-- StopIteration
              +-- StandardError
              |    +-- BufferError
              |    +-- ArithmeticError
              |    |    +-- FloatingPointError
              |    |    +-- OverflowError
              |    |    +-- ZeroDivisionError
              |    +-- AssertionError
              |    +-- AttributeError
              |    +-- EnvironmentError
              |    |    +-- IOError
              |    |    +-- OSError
              |    |         +-- WindowsError (Windows)
              |    |         +-- VMSError (VMS)
              |    +-- EOFError
              |    +-- ImportError
              |    +-- LookupError
              |    |    +-- IndexError
              |    |    +-- KeyError
              |    +-- MemoryError
              |    +-- NameError
              |    |    +-- UnboundLocalError
              |    +-- ReferenceError
              |    +-- RuntimeError
              |    |    +-- NotImplementedError
              |    +-- SyntaxError
              |    |    +-- IndentationError
              |    |         +-- TabError
              |    +-- SystemError
              |    +-- TypeError
              |    +-- ValueError
              |         +-- UnicodeError
              |              +-- UnicodeDecodeError
              |              +-- UnicodeEncodeError
              |              +-- UnicodeTranslateError
              +-- Warning
                   +-- DeprecationWarning
                   +-- PendingDeprecationWarning
                   +-- RuntimeWarning
                   +-- SyntaxWarning
                   +-- UserWarning
                   +-- FutureWarning
               +-- ImportWarning
               +-- UnicodeWarning
               +-- BytesWarning
"""

#记录错误
# err.py
import logging
logging.basicConfig(level=logging.INFO)#指定输出级别

class FooError(StandardError):
    pass
    
def foo(s):
    n=int(s)
    if n==0:
        raise FooError('invalid value: %s' % s) #自定义错误并抛出，不加对象则为向上抛出
    return 10 / n

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END'

#调试 1、print 2、断言
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!' #启动加入参数-o可以忽略assert
    return 10 / n

def main():
    foo('1')
main()

#3、logging 前面已导入
s = '2'
n = int(s)
logging.info('n = %d' % n)
print 10 / n

#4、pdb 麻烦
#5、pdb.set_trace
# err.py
import pdb

s = '1'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print 10 / n