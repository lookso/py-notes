#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from pkg.user import user
from pkg.setting import setting
import os

# str = input("按下 enter 键退出，其他任意键显示...\n")
#
# print(type(str))

def listT():

    list1 = ['runoob', 786, 2.23, 'john', 70.2]
    list2 = [1, 2, 3, 4, "7"]
    list1.append(list2)
    list = []
    list.extend(list1)
    print("list", list)
    for index in range(len(list)):
        print("list:", index, list[index])
    print("list slice", list[:3])
    print("-------------------------------list-------------------\n")
    return list


def tupleT():
    tuple = ('runoob', 786, 2.23, 'john', 70.2)
    print("range", range(1, 10, 2))
    print("john出现的次数:", tuple.count('john'))

    if 786 in tuple:
        print("exists")
    else:
        print("not exists")

    tinytuple = (123, 'john', ["name", 12], 12.993)

    k = 0
    for v in tuple:
        print("tuple k", k, v)
        k += 1
    return tinytuple + tuple


def dictT():
    newDict = {}
    dict = {"name": "jack", 1: "hello"}
    for k, v in dict.items():
        newDict[k] = v
    return newDict


def setT():
    # 要创建一个set，需要提供一个list作为输入集合,set可以看成数学意义上的无序和无重复元素的集合
    # 可以使用大括号 { } 或者 set() 函数创建集合，
    # 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
    s1 = set([1, 2, 3])
    s2 = set([3, 4, 5])
    print("交集", s1 & s2)
    print("并集", s1 | s2)
    if 2 in s1:
        s1.remove(2)
    for v in s1:
        print("set", v)


def main():
    print("-------------------------------list-------------------\n")
    listT()
    print("-------------------------------touple-------------------\n")
    tupleT()
    print("dict:", dictT())
    setT()
    setting.timeT()
    print("fbnq", setting.fbnq(5))


info = user.userInfo()
print("name", info['name'])

print(type(12))

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

print("-------------------------------main-------------------\n")
print("module name", __name__)

pid = os.fork()
if pid == 0:
    print("info", user.userInfo())
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

if __name__ == '__main__':
    main()
