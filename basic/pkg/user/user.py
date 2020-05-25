' user module '
__author__ = 'Michael Liao'

print("user module name",__name__)
def userInfo():
    info = {"name": "jack", "age": 21, "sex": "男"}

    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')
    print('END')

    return info


if __name__ == '__main__':
    userInfo()
