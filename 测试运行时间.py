"""
python 测试运行时间.py 200 200 200
"""

def test(reps, func, *args):
    import time
    start = time.clock()
    for i in range(reps):
        func(*args)
    return time.clock() - start

import 基于列表的栈类 as stack2
import 基于元组树的栈类 as stack3
import 基于列表的栈类2 as stack4

rept = 200
from sys import argv
pushes , pops, items = (int(arg) for arg in argv[1:])

def stackops(stackClass):
    x = stackClass('spam')
    for i in range(pushes): x.push(i)
    for i in range(items): t = x[i]
    for i in range(pops): x.pop()

for mod in (stack2, stack3, stack4):
    print('%s:' % mod.__name__, end = ' ')
    print(test(rept, stackops, getattr(mod, 'Stack')))