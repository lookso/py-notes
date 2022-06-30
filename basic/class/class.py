#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys
import logging

sys.path.append("/Users/lukun/apps/works/python/py_notes/basic")
print("sys.path:{}:".format(sys.path))

from pkg.setting import setting

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(lineno)d %(message)s",
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='w')


class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")


class Child(Employee):
    __private = 100  # 私有变量
    public = 200

    def __init__(self):
        self.sex = None
        self.age = setting.fbnq(10)

    def getAge(self):
        print("age", self.age)
        print("public", self.public)


def main():
    logging.debug("debug")
    print("Employee.__name__:", Employee.__name__)  # 类名
    print("Employee.__module__:", Employee.__module__)  # 模块名
    employee = Employee("jack", 11)
    employee.displayCount()
    employee.displayEmployee()

    c = Child()
    c.sex = "男"
    c.getAge()


class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

if __name__ == '__main__':
    main()
