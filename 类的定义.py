"""
抽象，特点抽象出来;
数据，也就是属性
行为，也就是方法

"""
class Person():
    pass
    #特殊方法是不要手动调用的
    # 特殊方法是可以在特殊时刻自动调用
    #init是在创建完对象后就立马执行，可以做初始化属性用
    #类后面的所有参数都会依次传入到init中
    # def __init__(self):


        # 在类中，我们所定义的变量，都是所有实例的公共属性
        #     a = 10
        #     b = 11
        #     name = "swk"
            #类中定义的函数就是方法
    def sayhello (self):
        print("hello,我是 %s" %self.name)

#创建实例
# p1 = Person()
# p2 = Person()
# print(p1.name,p2)
# p1.sayhello()
"""
方法调用会默认传入一个参数的，所以类中的函数没有传参，会报错。第一个参数由解释器传入，
Traceback (most recent call last):
  File "C:/Users/jinxiong/PycharmProjects/Python-Study/类的定义.py", line 20, in <module>
    p1.sayhello()
TypeError: sayhello() takes 0 positional arguments but 1 was given
swk <__main__.Person object at 0x000001891DE8D5E0>
"""
#实例为什么可以访问到类中定义的属性和方法？
#属性和方法的查找流程：
#调用时首先从当前对象中查找，如果当前对象没有就从所属类中查找，类中的属性是公共的，和实例中都可以保存属性，如果属性是所有实例对象共享的，应该就把他保存在类对象中，如果是某个独有的就放到自己实例对象中、
# 行为是一样的，但是数据都是有差异的，所以公共方法就放到类中，数据就放到独立实例中
#在方法中是不能直接使用类中的变量的
#方法每次被调用的时候，每次都会传入一个默认参数的，这个参数就是实例对象，一般把这个参数命名为self
#一般实例的属性是不需要共享的，所以一般属性是不在类中直接定义属性的，但是方法是基本都一样的，要就是功能基本都是一样的；

#我们希望，在用户创建对象是，必须设置name的属性，不设置就无法创建对象，这样就可以每次创建实例时提示用户来添加name的属性

# 魔术方法
class Dog():
    """
    dog类
    """
    def __init__(self,name,age,gender,height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def jiao(self):
        print('wangwangjiao')
    def yao(self):
        priint('yao')
    def run(self):
        print('run')

d =Dog("旺财",3,2,1)
print(d.name)
#属性不能随意修改，让你改就可以改，不让你改就不能改，如何实现？

#面向对象的三大特性之一：封装，封装是指的隐藏对象中一些不希望外部能访问到的属性和方法，使用封装增加了类的负责程度，但是确保了数据的安全性；
#如果希望属性是只读的，那就去掉setter方法，使用setter方法设置属性的时候，可以增加校验性，确保数据的安全正确性，可以使用getter和setter中添加其他动作；



#可以以双下划线开头的属性，来隐藏对象 
__name = "swk" # 实际上还是可以访问的，一般使用下划线开头的都是私有属性，一般不希望被修改。