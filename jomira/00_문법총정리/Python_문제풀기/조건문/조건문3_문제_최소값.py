'''
[최대값]
    [1] 숫자 3개를 랜덤으로 저장한다. (-100 ~ 100 사이의 숫자)
    [2] 3개의 랜덤 숫자를 비교한다.
    [3] 가장 작은 수(MIN)를 출력한다.    
'''

import random

a = random.randint(-100,100)
b = random.randint(-100,100)
c = random.randint(-100,100)

print(a,b,c)

minNum = a

if minNum > b :
    minNum = b
if minNum > c :
    minNum = c
    
print(minNum)