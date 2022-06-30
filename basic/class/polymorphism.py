class Animal(object):

    def run(self):
        print("Animal runing")


# 大类:
class Mammal(Animal):

    def run(self):
        print("Mammal runing")


class Human(object):

    def run(self):
        print("Human runing")


"""
多重继承
"""


# Mammal, Animal 继承顺序不要写错,Animal可以不用
class Dog(Mammal, Animal, Human):

    def run(self):
        super(Dog, self).run()
        print("Dog runing")


class Cat(Animal):

    def run(self):
        super().run()  # python3
        print("Cat runing")


class Tortoise(Animal):

    def run(self):
        print('Tortoise is running slowly...')


def run_twice(animal):
    animal.run()
    Human().run()


# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。interface
run_twice(Dog())

for x in (Dog(), Cat()):
    run_twice(x)
