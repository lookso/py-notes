#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys
import logging

sys.path.append("../../basic")
print("sys.path:{}:".format(sys.path))

from pkg.setting import setting

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(lineno)d %(message)s",
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='w')


class Employee(object):
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary, age):
        self.__age = age
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayAge(self):
        print("Age Employee %d" % self.__age)

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
        super(Child, self).displayCount()
        print("age", self.age)
        print("public", self.public)


def main():
    print('%s: %s' % ("汉尼拔", "拿破仑"))
    logging.debug("debug")
    print("Employee.__name__:", Employee.__name__)  # 类名
    print("Employee.__module__:", Employee.__module__)  # 模块名
    employee = Employee("jack", 11, 20)
    employee.displayCount()
    employee.displayEmployee()
    employee.displayAge()
    print("---------------------")
    c = Child()
    c.sex = "男"
    c.getAge()
    if isinstance(c, Child):
        print("c 是Child类的实例")


if __name__ == '__main__':
    main()
