'''
    [문제]
        [조건1] a, b 리스트 두 개에 1~100 사이의 랜덤 값 다섯 개를 저장한다.
        [조건2] base 변수에 랜덤으로 1~100 사이의 숫자를 저장한다. 
        base 변수값보다 큰 값들을 전부 출력하시오.
    [예시]
        base = 54

        a = [7, 99, 40, 14, 45]
        b = [46, 56, 87, 7, 80]

        99
        56
        87
        80    
'''

import random

a = []
b = []

base = random.randint(1,100)
print(base)

for i in range(5) :
    a.append(random.randint(1,100))
    b.append(random.randint(1,100))
    
print(a)
print(b)

size = len(a)
for i in range(size) :
    if a[i] > base or b[i] > base:
        print(a[i])
        print(b[i])