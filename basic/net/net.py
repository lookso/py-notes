from urllib import request

try:
    with request.urlopen('https://www.baidu.com/') as f:

        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))
except BaseException as e:
    print(e)
finally:
    print("end")
