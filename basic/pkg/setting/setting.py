import time
import json

print("setting module name",__name__)

from pkg.user import user

print("user-info",user.userInfo())

def timeT():
    global json
    ticks = time.time()
    print("timestamp", ticks)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    jsonData = '{"a":"1","b":2,"c":3,"d":4,"e":5}'

    text = json.loads(jsonData)
    print("text", text)

    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    json = json.dumps(data)
    print(json)


def fbnq(n):
    if n < 2:
        return 1
    return fbnq(n - 1) + fbnq(n - 2)

if __name__ == '__main__':
    print("name",__name__)


