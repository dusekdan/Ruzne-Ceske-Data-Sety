import operator
from random import randrange, choice

count = 500
FILENAME = "equations2.txt"
HIGH_BOUND = 1000
OPS = { '+': operator.add, '-': operator.sub } # '*': operator.mul, '/' : operator.truediv }

def gen_equation():
    opX = randrange(HIGH_BOUND)
    opY = randrange(HIGH_BOUND)
    operator = choice(list(OPS.keys()))
    result = OPS[operator](opX,opY)
    return f"{opX} {operator} {opY} = ? | {result}"

with open(FILENAME, 'w') as f:
    for i in range(count):
        f.write(gen_equation() + '\n')