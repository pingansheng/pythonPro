#coding: gbk

print 'hello world'
print 'The quick brown fox',    'jumps over', 'the lazy dog'
name=raw_input('please enter your name:')
print 'hello',name


print '\\\t\\'
print r'\\\t\\' #��ʾ������ת��
print 'I\'m \"OK\"'


print '''line1
line2
line3'''  #��ʾ�������ݣ�ʡȥд\n

print len('����')
print len(u'����')

#��ʽ������ַ���
print 'Hi, %s, you have $%d.' % ('Michael', 1000000)
print '%2d-%03d' % (3, 1)
print '%.2f' % 3.1415926

#LIST
classmates = ['Michael', 'Bob', 'Tracy']
classmates.sort() #����
print len(classmates)
print classmates[0]
print classmates[-1] #ֱ�ӻ�ȡ���һ��Ԫ�أ��Դ����ƣ����Ի�ȡ������2��[-2]��������3��[-3]
classmates.append('Adam')
classmates.insert(1,'Jack')
classmates.pop() #ɾ�����һ��Ԫ��
classmates.pop(1) #ɾ����i+1��Ԫ��

print classmates

#tuple һ�����岻�ɸı�

classmates = ('Michael', 'Bob', 'Tracy')

t=(1,) #һ��Ԫ�ص�tuple���巽ʽ������С��������
#һ�ֿɱ��tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t



#����
age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'

birth = int(raw_input('birth: ')) #raw_input()������Զ��string
if birth < 2000:
    print '00ǰ'
else:
    print '00��'

#ѭ��
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

sum = 0
for x in range(101):  #range(m)����0-(m-1)������
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

#�ж��Ƿ����key
print 'Thomas' in d
if 'Thomas' in d:
    print d['Thomas']
if d.get('Thomas') != None:
    print d['Thomas']
else:
    print None
#key�����ǲ��ɱ����,�ַ����������Ⱦ��ǣ����ɱ��������󲻸ı�����

#SET �������ظ�
s = set([1, 2, 3])
s = set([1, 1, 2, 2, 3, 3])
s.add(4)
s.remove(4)

s1=set([1,2,3])
s2=set([1,2,4])
print s1 & s2 #����
print s1 | s2 #����


#����
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

#�պ���
def nop():
    pass
#pass����һ����;
if age >= 18:
    pass

#����������ĺ���
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#�������ֵ�ĺ����������Ϸ��ص���tuple��
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

#����Ĭ�ϲ���
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

enroll('Adam', 'M', city='Tianjin') #����ʱ����ָ��ĳ���̶�����


def add_end(L=None): #Ĭ�ϲ�������ָ�򲻿ɱ���󣬷���ÿ�ε��ú�����Ĭ�ϲ�����ֵ����ı�
    if L is None:
        L = []
    L.append('END')
    return L

#�����ɱ����

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1,2,3)

nums = [1, 2, 3]
calc(*nums) #��List����triple��Ϊ�ɱ����

#�ؼ��ֲ���,�����㴫��0������������������Ĳ���(���ڷ�װdict)

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
#�ؼ��ֲ����ں����ڲ��Զ���װΪһ��dict

person('Bob', 35, city='Beijing')
#name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer')
#name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

#�������dict����
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)
#name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
#name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

#����������ϣ����ֺ�������ͬʱʹ��

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

#���������ʹ��triple��dict����
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)
#a = 1 b = 2 c = 3 args = (4,) kw = {'x': 99}
#���ԣ��������⺯����������ͨ������func(*args, **kw)����ʽ���������������Ĳ�������ζ���ġ�

##��������С��
#Python�ĺ������зǳ����Ĳ�����̬���ȿ���ʵ�ּ򵥵ĵ��ã��ֿ��Դ���ǳ����ӵĲ�����
#Ĭ�ϲ���һ��Ҫ�ò��ɱ��������ǿɱ�������л����߼�����
#Ҫע�ⶨ��ɱ�����͹ؼ��ֲ������﷨��
#*args�ǿɱ������args���յ���һ��tuple��
#**kw�ǹؼ��ֲ�����kw���յ���һ��dict��
#�Լ����ú���ʱ��δ���ɱ�����͹ؼ��ֲ������﷨��
#�ɱ�����ȿ���ֱ�Ӵ��룺func(1, 2, 3)���ֿ�������װlist��tuple����ͨ��*args���룺func(*(1, 2, 3))��
#�ؼ��ֲ����ȿ���ֱ�Ӵ��룺func(a=1, b=2)���ֿ�������װdict����ͨ��**kw���룺func(**{'a': 1, 'b': 2})��
#ʹ��*args��**kw��Python��ϰ��д������ȻҲ�����������������������ʹ��ϰ���÷���
#β�ݹ飬returnֻ���غ���

#��Ƭ���� [��ʼ:����:����]
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L[0:3] #������0��ʼ��ȡǰ����
print L[:3] #����Ϊ0�ɺ���
print L[1:3] #������1��ʼ��ȡǰ����
print L[-2:] #�ӵ����ڶ�����ʼ��ֱ�����
print L[-2:-1] #�ӵ����ڶ�����ʼ��ֱ������ǰһ��
L = range(100)
print L[:10] #ǰ10����
print L[-10:] #��10����
print L[10:20] #��11��������20��
print L[:10:2] #ǰ10����ÿ��2��ȡһ��
print L[::5] #ÿ��5��ȡһ��
print L[:] #�����������

#triple���ַ����Ⱦ���ʹ����Ƭ
print (0, 1, 2, 3, 4, 5)[:3]
print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]

#����
d = {'a': 1, 'b': 2, 'c': 3}

print "����Dict��Key"
for key in d:
     print key

print "����Dict��Value"
for value in d.itervalues():
     print value

print "ͬʱ����Dict��Key��Value"
for key,value in d.iteritems():
     print key,value

print "�����ַ���"
for ch in 'ABC':
     print ch
#�ж�һ�������Ƿ�ɵ���
from collections import Iterable
print isinstance('abc', Iterable) # str�Ƿ�ɵ���
#True
print isinstance([1,2,3], Iterable) # list�Ƿ�ɵ���
#True
print isinstance(123, Iterable) # �����Ƿ�ɵ���
#False

#Python���õ�enumerate�������԰�һ��
#list�������-Ԫ�ضԣ������Ϳ�����forѭ��
#��ͬʱ����������Ԫ�ر���

list=['A','B','C']
for i, value in enumerate(list):
    print i, value

#�б�����ʽ
print range(1, 11)

print [x * x for x in range(1, 11)]

print [x * x for x in range(1, 11) if x % 2 == 0] #���������ж�

print [m + n for m in 'ABC' for n in 'XYZ'] #����ѭ������ȫ����

#ʾ�����г�Ŀ¼�����ļ�
import os # ����osģ��
print [d for d in os.listdir('C:\\')] # os.listdir�����г��ļ���Ŀ¼

#forѭ������ʹ�ö������
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.iteritems():
    print k, '=', v

#�б�����ʽҲ����ʹ����������������list��
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k + '=' + v for k, v in d.iteritems()]

#list�����ַ�����Сд
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]
#isinstance�������ж����ݵ������������������ж��ַ���isinstance(a,str)
print isinstance(12.1,int)

#������generator������ʹ��ʱ����������Ԫ�أ���ʡ�ռ�
L = [x * x for x in range(10)]
g = (x * x for x in range(10)) #�б���������Ϊ()���Ǵ���generator
#generator.next()�������Եõ�Ԫ�أ�һ��ʹ��forѭ������
for n in g:
    print n
#�ڶ��д�����ʽ��������ʹ��yield�ؼ���
#쳲��������к�����generator�ĺ���ÿ�ε���next()��ʱ��ִ�У�����yield��䷵�أ�
#�ٴ�ִ��ʱ���ϴη��ص�yield��䴦����ִ�С�һ��ʹ��forѭ��ִ��
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for i in fib(10):
    print i

#����ʽ���
#��������ָ����
f=abs
print f(-5)

#map/reduce����

#map()������������������һ���Ǻ�����һ�������У�
#map������ĺ����������õ����е�ÿ��Ԫ�أ����ѽ����Ϊ�µ�list���ء�

def f(x):
    return x**2

a=map(f,[1,2,3,4,5,6,7,8,9])
print a;

def check(s):
    return s[0].upper()+s[1:].lower()
name=['adam', 'LISA', 'barT']
print map(check,name)

#reduce��һ������������һ������[x1, x2, x3...]�ϣ�����������������������
#reduce�ѽ�����������е���һ��Ԫ�����ۻ�����
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def add(x, y):
    return x + y

print reduce(add, [1, 3, 5, 7, 9]) #((((1+3)+5)+7)+9)

#����reduce���
def prod(A=[]):
    return reduce(lambda x,y:x*y,A)
print prod([1,2,3,4,5,6,7,8,9,10])

#���ʹ��
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
   '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def fn(x, y):
    return x * 10 + y
print reduce(fn, map(char2num, '13579'))
#�ַ���ת��������map(char2num, '13579')=[1,3,5,7,9]

#filter��������������
def is_odd(n):
    return n % 2 == 1

print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])

#sorted����

print sorted([6,5,4,3,2,1])


#���Դ��뺯�����бȽ�
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
	
print sorted([36, 5, 12, 9, 21], reversed_cmp)

#���Դ�Сд���ַ���������
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)	
		
#������Ϊ����ֵ
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print f()
#�ڲ�����sum�����ⲿ����lazy_sum�Ĳ����;ֲ�����
#lazy_sum���غ���sumʱ����ز����ͱ����������ڷ��صĺ�����,��Ϊ���հ���

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1(),f2(),f3()#9,9,9
#���صĺ��������˱���i��������������ִ�С��ȵ�3������������ʱ��i�Ѿ������3��������ս��Ϊ9��
#ʹ�ñհ�ʱ�򣺷��غ�����Ҫ�����κ�ѭ�����������ߺ����ᷢ���仯�ı�����
#�������:��Ӻ����ò�����(���������󶨺󲻸ı�)����ʹ��lambda�������̴���

#����������lambda��ʾ��������
map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
f = lambda x: x * x#���Ը�ֵ
def build(x, y):
    return lambda: x * x + y * y#���Է���
	
#װ����	
#������һ�����󣬺���������Ա���ֵ�����������ԣ�ͨ������Ҳ�ܵ��øú�����
def now():
    print '2013-12-25'
f = now
f()#2013-12-25
print now.__name__#������name����
print f.__name__
#��ǿnow()�����Ĺ��ܣ��ں�������ǰ���Զ���ӡ��־����ϣ���޸�now()�����Ķ���
#�����ڴ��������ڼ䶯̬���ӹ��ܵķ�ʽ����֮Ϊ��װ��������Decorator��

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log#ʹ��@����װ����
def now():
    print '2013-12-25'
now()#now = log(now)

#��Ҫ������װ����
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

#ʹ��װ��������name���Ա仯��ʹ��funtools������һ��������װ��������
#@functools.wraps(func)����wrapper����֮ǰ

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

#���ַ�ʽ����Ӧǰ���ӡ��־
def log(text_fun):#�˲���Ϊָ�����ı����ߺ�����
    if isinstance(text_fun,str):
        def decorator(func):#��text_funΪ�ı�����funcΪ�ڶ�������������
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print 'before',"".join(text_fun)
                func(*args, **kw)
                print 'after',"".join(text_fun)
            return wrapper
        return decorator
    else:#�˴���������text_funһ��
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


#ƫ����������functools
print int('123',base=8)#��8���ƽ���ת��
#����ƫ������
int2 = functools.partial(int, base=2)
print int2('10101010')


#ģ�飬��moudle.py

#�������

class Student(object):#�����ڱ�ʾ�̳�

    def __init__(self, name, score):#���캯�����׸�����Ϊself
        self.name = name
        self.__score = score#˽�б����������Կ���ͨ��xx._Student_name���ʣ�������
							#���»���_name������ʾ������ֱ�ӷ��ʣ���Ȼ����

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

#��ȡ������Ϣ
print type(a)

print type(a)==type(d)

import types

print type(Animal)==types.TypeType
#type(int)==type(str)==types.TypeType True���ͱ����������TypeType

#isinstance
print isinstance(d,Animal)

print isinstance(12,(int,str,Animal))#�ж�12�ǲ�������һ��

#dir()��ӡ�������������뷽��,������������
print dir('ABC')

#�õ���������״̬
if hasattr(d,'age'):
    print d.age
else:
    setattr(d,'age',19)
    print d.age 

print getattr(d,'z','null')#��ȡ����'z'����������ڣ�����Ĭ��ֵnull

#��÷���
fn=getattr(d,'run')
fn()

#�������߼�

d.name = 'Michael' # ��̬��ʵ����һ������

def set_age(self, age): # ����һ��������Ϊʵ������
    self.age = age

from types import MethodType
d.set_age = MethodType(set_age,d, Dog) # ��ʵ����һ������,������ʵ����������
d.set_age(20)
print d.age

Dog.set_age = MethodType(set_age, None, Dog) # ����󶨣�����ʵ��������

# __slots__����������������Ժ�����ӵ�����
class Student(object):
    __slots__ = ('name', 'age') # ��tuple��������󶨵���������
s=Student()
s.age=15
#���� s.score=20

#���಻�����ã�������������Ҳ����__slots__����������������Ծ��������__slots__���ϸ����__slots__


class Student(object):

    @property #��һ������������Ե���
    def score(self):
        return self._score

    @score.setter #setter��Ϊ���Ը�ֵ
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s=Student()
s.score=100
print s.score

#s.score=200 ����

#���ؼ̳�

class Flyable(object):
    def fly(self):
        print('Flying...')

class Bird(Animal,Flyable):
    pass
    
B=Bird()
B.fly()
#һ�����ֹ��ܳ�ΪMixin������Ϊ FlyableMixin

#�����࣬ʵ������Java toString()�ȷ���
#__len__()<=>len()
#__str__()<=>print ...
#__repr__(),ʹ�ö��������ã����ص�����Ϣ��һ��  __repr__ = __str__
#__iter__���� for in����
#__getitem__�±�ȡԪ��
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # ��ʼ������������a��b

    def __iter__(self):
        return self # ʵ��������ǵ������󣬹ʷ����Լ�

    def next(self):
        self.a, self.b = self.b, self.a + self.b # ������һ��ֵ
        if self.a > 100000: # �˳�ѭ��������
            raise StopIteration();
        return self.a # ������һ��ֵ

    def __getitem__(self, n):
        if isinstance(n, int):#�±�
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):#��Ƭ����
            start = n.start
            stop = n.stop
            step=n.step
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            L=L[::step]#����step
            return L
F=Fib()
for n in F:
    print n
    
print F[5]
print F[0:5]
print F[0:5:2]

#__getattr__  ���ò����ڵ�����ʱ��Python����������ͼ����__getattr__(self, 'XXX')�����Ի������

class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
S=Student()
print S.age()
#print S.pp

#��ʽ����
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
#c.status����__getattr__����һ������ʵ�������Կ��Ե���__call__()
print c.status('����',statuscode=200).timeline.list('pingansheng')

#__call__ֱ�Ӷ�ʵ�����е���
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
        
s = Student('Michael')
s()
#Callable���ж϶����Ƿ�Ϊ���������__call()__��ʵ��
print callable(s)

#��̬���Ե��У���������Ķ�����������ʱ������
#�����ķ�������type(),������type()��������һ����
def fn(self,name='world'):
    print('Hello ,%s'  % name)
Hello=type('Hello',(object,),dict(hello=fn)) #(�����ƣ�����triple�����������뺯���İ�)
h=Hello()
h.hello()
print type(Hello)
print type(h)

#metaclass�����ڴ����붯̬�ı��౾���Թ�


#���󡢵��ԺͲ���

try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else: #δ�����쳣ִ��
    print 'no error!'
finally:
    print 'finally...'
print 'END'
#�쳣�̳���
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

#��¼����
# err.py
import logging
logging.basicConfig(level=logging.INFO)#ָ���������

class FooError(StandardError):
    pass
    
def foo(s):
    n=int(s)
    if n==0:
        raise FooError('invalid value: %s' % s) #�Զ�������׳������Ӷ�����Ϊ�����׳�
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

#���� 1��print 2������
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!' #�����������-o���Ժ���assert
    return 10 / n

def main():
    foo('1')
main()

#3��logging ǰ���ѵ���
s = '2'
n = int(s)
logging.info('n = %d' % n)
print 10 / n

#4��pdb �鷳
#5��pdb.set_trace
# err.py
import pdb

s = '1'
n = int(s)
pdb.set_trace() # ���е�������Զ���ͣ
print 10 / n