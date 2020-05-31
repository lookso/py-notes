#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 判断是否是回文字符串
def Palindrome(str):
    if len(str) < 2:
        return True

    if str[0] != str[-1]:
        return False
    else:
        # 字串符的第一项和最后一项等同,所以去除字符串的第一项和最后一项,继续进行检查
        return Palindrome(str[1:-1])


def main():
    print("是否是回文字符串:{}".format(Palindrome("abcbaabcba")))


if __name__ == '__main__':
    main()
