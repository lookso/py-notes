#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Basic:
    pass


class Pytype(Basic):

    def __init__(self, tupleData, listData, setData, dictData):
        self.tupleData = tupleData
        self.listData = listData
        self.setData = setData
        self.dictData = dictData

    def handleTuple(self):
        tupleData = self.tupleData
        tupleData = tupleData + (100, )
        print("tuple:{}".format(tupleData))

    def handleList(self):
        l = self.listData
        l.append(55)
        l.remove(55)
        l.append([100, 200, 300])
        print("list:{},len:{}".format(l, len(l)))

    def handleSet(self):
        print("set:{}".format(self.setData))

    def handleDict(self):
        # 字典是完全无序的映射集合
        dictData = self.dictData
        dictData["nb"] = "nx"
        print("dict:{}".format(dictData))

        if "a" in dictData:
            print("a exists")

        if dictData.get('nb'):
            print("this nb exists")

    def __del__(self):
        print("调用__del__() 销毁对象，释放其空间")


tupleData = ("a", "b", "c", 1, 2, 3)
listData = [1, 2, 3]
setData = (
    "a",
    "b"
    "c",
    1,
    2,
    3,
    4,
    4,
)
dictData = {"a": 1, "b": 2, 3: 3}
pyType = Pytype(tupleData, listData, setData, dictData)
pyType.handleTuple()
pyType.handleList()
pyType.handleSet()
pyType.handleDict()
