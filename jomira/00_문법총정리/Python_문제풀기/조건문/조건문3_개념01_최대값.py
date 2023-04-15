'''
[최대값]
    [1] 숫자 3개를 랜덤으로 저장한다. (1~1000 사이의 숫자)
    [2] 3개의 랜덤 숫자를 비교한다.
    [3] 가장 큰 수(MAX)를 출력한다.    
'''

import random

a = random.randint(1,1000)
b = random.randint(1,1000)
c = random.randint(1,1000)

print(a,b,c)

max = a

if max < b :
    max = b
if max < c :
    max = c
    
print(max)