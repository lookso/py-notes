def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)


def yield_test():
    x=1
    a=1
    yield x
    x=x+1
    a=a+1
    print("a:%s" %a)
    

print(next(yield_test()))
for x in yield_test():
    print(x)

def fab(max):
    n, a, b = 0, 0, 1 
    while n < max: 
        print("n:%s,b:%d" %(n,b))
        yield b      # 使用 yield
        # print b 
        a, b = b, a + b
        n = n + 1
 
for n in fab(5):
    print (n)

  

