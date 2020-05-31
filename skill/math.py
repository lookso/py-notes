import random
import re

list1 = None
list2 = None

if (not list1 and list2):
    print(123)
else:
    print(345)

name = "hello".join("123").join("456")
print(name)

print("----------------------------------\n")

response = dict()

outIntermMessages = []

a = random.randint(1, 999)
b = random.random()
ops = ['+', '-', '*', '/']
op = ops[random.randint(0, 3)]
expression = "{0}{1}{2:.03f}".format(a, op, b)
result = str(eval(expression))
msg = "我知道 {0} = {1} 。".format(expression, result)
msg2 = "你接着出题考我吧。"

response['textOutput'] = msg + msg2

print(response)
print("\n")


class DialogMath:
    nums = [
        ('.', ['.', '点']),
        ('0', ['零', '〇', '０']),
        ('1', ['一', '壹', '１']),
        ('2', ['二', '贰', '２', '两', '貳', '貮', '俩']),
        ('3', ['三', '叁', '３']),
        ('4', ['四', '肆', '４']),
        ('5', ['五', '伍', '５']),
        ('6', ['六', '陆', '６']),
        ('7', ['七', '柒', '７']),
        ('8', ['八', '捌', '８']),
        ('9', ['九', '玖', '９'])
    ]

    scales = [
        ('1', ['.', '点']),
        ('10', ['十', '拾']),
        ('100', ['百', '佰']),
        ('1000', ['千', '仟']),
        ('10000', ['万', '萬']),
        ('100000000', ['亿', '億']),
        ('1000000000000', ['兆'])
    ]

    unaryOperators = [
        ('sqrt2p', ['根号']),
        ('sqrt2', ['平方根', '开方']),
        ('sqrt3', ['立方根']),
        ('sqrt', ['次方根']),
        ('pow', ['次方', '次幂', ]),
        ('pow2', ['平方']),
        ('pow3', ['立方', '幂']),
        ('opposite', ['负']),
        ('factorial', ['阶乘']),
        ('sin', ['正弦']),
        ('cos', ['余弦']),
        ('tan', ['正切']),
        ('cot', ['余切']),
        ('pi', ['π']),
        ('log', ['log'])
    ]

    binaryOperators = [
        ('+', ['加', '＋']),
        ('-', ['减', '－']),
        ('*', ['乘以', '乘', '×']),
        ('/', ['除以', '除', '比', '÷', '：', ':']),
        (':', ['分之']),
        ('(', ['左括号', '(', '（', '(', '（']),
        (')', ['右括号', ')', '）', ')', '）'])
    ]

    mathFeatures = [
        '=',
        '＝',
        '是(几|多少)',
        '为',
        '得',
        '等',
        '得到',
        '等于'
    ]

    specWords = [
        '的',
        '开'
    ]

    substitutes = {

        '乘乘': '乘'
    }

    interfereWord = [
        "一下",
        "一猜",
    ]

    blackList = [
        "年", "月", "周", "星期", "日", "天", "时", "分", "秒",
        "你和", "和你",
        "元", "钱", "币",
        "三围"
    ]

    replyPrefix = ["这个难不倒我，"]

    defaultTextOutput = [
        "我只听到了一个数字，你说的太快啦，慢一点说吧",
    ]

    def __init__(self):

        self.allOperators = []
        self.allNums = []
        self.arabiaNums = []

        for operator in self.unaryOperators:
            self.allOperators.append(operator[0])
            self.allOperators.extend(operator[1])

        for operator in self.binaryOperators:
            self.allOperators.append(operator[0])
            self.allOperators.extend(operator[1])

        for num in self.nums:
            self.allNums.append(num[0])
            self.allNums.extend(num[1])
            self.arabiaNums.extend(num[0])

        for num in self.scales:
            self.allNums.extend(num[1])

        self.patternNum = re.compile('|'.join(self.allNums).replace('.', '\.'))
        print("self.patternNum", self.patternNum, "\n")
        self.patternArabiaNum = re.compile('|'.join(self.arabiaNums).replace('.', '\.'))
        print("self.patternArabiaNum", self.patternArabiaNum, "\n")
        self.patternOp = re.compile(
            '(' +
            '|'.join(self.allOperators)
            .replace('+', '\+').replace('-', '\-').replace('*', '\*').replace('(', '\(').replace(')', '\)') +
            ')')
        print("self.patternOp", self.patternOp, "\n")
        self.patternEq = re.compile('|'.join(self.mathFeatures))
        print("self.patternEq", self.patternEq, "\n")
        self.patternSpec = re.compile('|'.join(self.specWords))
        print("self.patternSpec", self.patternSpec, "\n")
        self.patternInterfere = re.compile('|'.join(self.interfereWord))
        print("self.patternInterfere", self.patternInterfere)
        self.patternBlackList = re.compile('|'.join(self.blackList))

        print("self.patternBlackList", self.patternBlackList)

math = DialogMath()
