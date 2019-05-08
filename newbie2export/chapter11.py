# LOOK 面向对象编程 OOP
"""
OOP的三个基本特性：封装性、继承性和多态性
封装性：把复杂封装起来，对外提供接口
继承性：一般类和特殊类
多态性：子类具有不同的状态或行为
"""

""" 类的定义和使用
    class 类名[ (父类) ]
        类体

class Animal(object):
    # 类体
    pass
animal = Animal()
"""

"""类的成员
类成员：成员变量(attribute)、属性(property)、成员方法
成员变量：实例变量、类变量
成员方法：实例方法、类方法、静态方法
attribute 往往会提供一些setter、getter访问器，翻译成“成员变量”比较贴切
property 属性，本质上就是setter、getter访问器
"""
# 实例变量
class Animal(object):
    """定义动物类"""

    def __init__(self, age, sex, weight):
        self.age = age        # 实例变量
        self.sex = sex
        self.weight = weight 

animal = Animal(2, 1, 10.0)
print('年龄:{0},性别：{1},体重：{2}'.format(animal.age,animal.sex,animal.weight))

"""类变量
    类变量是所有实例共有的相同属性，实例变量是个体拥有的属性
    不要通过实例存取类变量数据
    通过实例读取变量时，Python会先在实例中找，没找到再到类中去找
    当通过实例为变量赋值时，无论类中是否有该同名变量，Python都会创建一个同名实例变量
"""
class Account:
    """定义银行账户类"""

    interest_rate = 0.0668    #类变量

    def __init__(self, owner, amount):
        self.owner = owner    #实例变量
        self.amount = amount

account = Account('Tony',1_800_000.00)
print('账户名：{0},账户金额：{1},利率：{2}'.format(account.owner,
            account.amount,account.interest_rate))
print('Account 利率：{0}'.format(Account.interest_rate))

# 解释器会在实例中查找account.interest_rate,没找到，就去Account中找
print('acl 利率: {0}'.format(account.interest_rate))
print('acl 实例所有变量:{0}'.format(account.__dict__))

# 这样的操作，无论是否有同名类变量都会创建一个新的实例变量。
# 这些动态创建的变量无法通过类中的方法访问
account.interest_rate = 0.01
account.interest_rate2 = 0.01
print('acl 实例所有变量:{0}'.format(account.__dict__))


"""构造方法 __init__()
   也属于魔法方法。
   第一个参数应该是self

   def __init__(self, age, sex=1, weight=0.0):
       self.age = age
       self.sex = sex
       self.weight = weight

"""

"""实例方法
    实例方法与实例变量一样都是某个实例个体特有的。
    方法是在类中定义的函数
    定义实例方法时第一个参数也应该是 self，这个过程是将当前实例与该方法绑定，使其成为实例方法
"""    
class Animal1(object):
    """定义动物类"""

    def __init__(self, age, sex=1, weight=0.0):
        self.age = age    #实例变量
        self.sex = sex
        self.weight = weight

    # eat(self) self 定义实例方法
    def eat(self):
        self.weight += 0.05
        print('eat...')

    def run(self):
        self.weight -= 0.01
        print('run...')

al = Animal1(2, 0, 10.0)
print('a1 体重：{0:0.2f}'.format(al.weight))
al.eat()
print('a1 体重：{0:0.2f}'.format(al.weight))
al.run()
print('a1 体重：{0:0.2f}'.format(al.weight))


"""类方法
    类方法与类变量类似，都属于类，不属于个体实例
    类方法不需要与实例绑定，但是需要与类绑定
    他的第一个参数不是 self,而是类的 type实例，
    type 是描述 Python数据类型的类，所有数据类型都是 type的一个实例
    注：类方法可以访问类变量和其他类方法，但不能访问其他实例方法和实例变量
"""
class Account1:
    """定义银行账户类"""

    interest_rate = 0.0668    #类变量

    def __init__(self, owner, amount):
        self.owner = owner    #实例变量
        self.amount = amount
    
    # 类方法
    # cls 是 type类型，是当前Account1 类型的实例
    # @classmethod 装饰器，声明该方法是类方法。
    @classmethod
    def interest_by(cls, amt):

        # cls.interest_rate 代表访问的是类变量
        return cls.interest_rate * amt

interest = Account1.interest_by(12_000.0)
print('计算利息:{0:.4f}'.format(interest))

"""静态方法
    如果定义的方法，既不想和实例绑定，也不想和类绑定，那就静态方法
    调用静态方法和类方法相同可以通过类名实现，也可通过实例调用
    静态方法和类的耦合度更加松散
    在一个类中定义静态方法只是为了提供一个基于类名的命名空间
"""
class Account2:
    """定义银行账户类"""

    interest_rate = 0.0668    #类变量

    def __init__(self, owner, amount):
        self.owner = owner    #实例变量
        self.amount = amount
    
    # 类方法
    @classmethod
    def interest_by(cls, amt):
        return cls.interest_rate * amt

    # 静态方法
    @staticmethod
    def interest_with(amt):
        return Account2.interest_by(amt)

interest1 = Account1.interest_by(12_000.0)
print('计算利息:{0:.4f}'.format(interest1))
interest2 = Account2.interest_with(12_000.0)
print('计算利息:{0:.4f}'.format(interest2))


"""封装性
    python 没有与封装性相关的关键字，通过特定的名称实现对变量和方法的封装。

    私有变量：在变量的前面加双下划线 __ ,只能在类的内部访问，不可通过实例访问。
            python的私有变量只是形式上的限制，依靠自觉，非强制性。

    私有方法：和变量类似。
"""

"""继承性
   多态性的前提是继承性
   字类继承父类只是继承父类中的成员变量和方法，不能继承私有的成员变量和方法。
"""

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def info(self):
        template = 'Person [name={0}, age={1}]'
        s = template.format(self.name, self.age)
        return s

class Student(Person):

    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school


""" 子类重写父类的方法(Override)
    如果子类的方法名和父类相同，而且参数也相同，那么子类重写了父类的方法
"""

""" 多继承
    一个子类多个父类
    python解决方法名字冲突的方案：当子类实例调用方法时，先从子类找，如果没有，就按照
    父类列表从左到右的顺序找，如果没有再找父类的父类。
"""

"""多态性
    发生多态性的两个前提：1、继承 2、重写
    多态发生时，解释器根据引用指向的实例调用它的方法 
    多态性对于动态语言Python而言意义不大。

    issubclass(Ellipse, Figure)  是否是Figure的子类
"""

"""鸭子类型
    在动态语言中有一种类型检查称为“鸭子类型”，即一只鸟走起来、游起来、叫起来像鸭子，
    那它就可以被当作鸭子。
"""
class Animal2(object):
    def run(self):
        print('动物跑...')
    
class Dog(Animal2):
    def run(self):
        print('狗狗跑...')

class Car:
    def run(self):
        print('汽车跑...')

def go(al):
    al.run()

go(Animal2())
go(Dog())   
go(Car())

"""Python 的根类 :object
   所有类的根类
   __str__(): 返回该对象的字符串表示
   __eq__(other):当使用 '=='来比较两个对象时，指示其他对象是否与此对象“相等”
   这些方法需要在子类中重写。

"""
class Person1:

    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def __str__(self):
        template = 'Person [name={0}, age={1}]'
        s = template.format(self.name, self.age)
        return s

person = Person1('Tony', 18)
print()
print(person)

class Person2:

    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def __str__(self):
        template = 'Person [name={0}, age={1}]'
        s = template.format(self.name, self.age)
        return s
    
    def __eq__(self,other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False

p1 = Person2('Tony',18)
p2 = Person2('Tony',18)
print()
print(p1 == p2)


"""枚举类
    枚举是用来管理一组相关的有限个常量的集合
    使用枚举可提高程序的可读性，特别实在比较时
    它本质上是一种类

    class 枚举类名(enum.Enum):
        枚举常量列表

    可以使用enum.IntEnum 限制每一个常量为整形
    可以使用 @enum.unique装饰器，限制常量成员唯一
"""
import enum

@enum.unique
class WeekDays(enum.IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5

day = WeekDays.FRIDAY
print()
print(day)
print(day.value)
print(day.name)
if day == WeekDays.MONDAY:
    print('working...')
elif day == WeekDays.FRIDAY:
    print('studing')
