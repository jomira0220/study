'''
    [문제]
        [조건1] 리스트에 랜덤 숫자(1~100) 5개를 추가한다.
        [조건2] 위 값 중에 50보다 큰 값들만 출력한다.
    [예시]
        arr = [84, 28, 5, 100, 80]
        84
        100
        80
'''

import random

arr = []

for i in range(5) :
    arr.append(random.randint(1,100))
    if arr[i] > 50 : print(arr[i])
    
print(arr)