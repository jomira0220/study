'''
    [문제]
         a이차리스트에 랜덤숫자(1~100)을 9개 저장하고,
         그리고 가장 큰 값을 출력하시오.
    [예시]
        [5, 81, 71]
        [49, 85, 29]
        [63, 54, 27]
        
        max :  85
'''

import random

a = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

max = 0
size = len(a)
for i in range(size) :
    for j in range(size) :
        a[i][j] = random.randint(1,100)
        if max < a[i][j] :
            max = a[i][j]
    print(a[i])
    
print(max)