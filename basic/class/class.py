#!/usr/bin/python
# -*- coding: UTF-8 -*-
from math.pkg import setting

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


print("Employee.__name__:", Employee.__name__)  # 类名
print("Employee.__module__:", Employee.__module__)  # 模块名
employee = Employee("jack", 11)
employee.displayCount()
employee.displayEmployee()

c = Child()
c.sex = "男"
c.getAge()
