#coding=utf8
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    """An example of class"""
    pass 
##空语句，为了保持程序结构的完整性，可要可不要

## class Dog 继承动物类
class Dog(Animal):

    def __init__(self, name):
        ## 初始化name
        self.name = name

## Cat 继承 Animal类
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        #继承了Person
        super(Employee, self).__init__(name)
        ## 添加新的类成员变量
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = 'rover'
print frank.pet,frank.salary,frank.name

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()