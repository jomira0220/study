'''
    [문제]
        [1] 1~50 사이의 랜덤 숫자 중 3의 배수 3개의 합을 total에 추가한다. 
        [2] 위 내용을 총 다섯 번 반복한다. 
        [3] 합이 가장 큰 수를 변수 max에 저장하시오.
    [예시]
        27 27 18 = 72
        30 24 15 = 69 
        6 12 45 = 63  
        45 27 48 = 120
        30 18 27 = 75 
        
        max = 120
'''

import random

total = []
max = 0

for i in range(5) :
    count = 0
    while True :
        num = random.randint(1,50)
        totalNum = 0
        if num % 3 == 0 :
            print(num,end=' ')
            totalNum += num
            count += 1
            if count == 3 : 
                print(f' = {totalNum}')
                total.append(totalNum)
                break
    max += totalNum
    
print(f'total = {total}')
print(f'max = {max}')
print(f'max = {sum(total)}') # 리스트 값 모두 합친값 리턴함수

    
