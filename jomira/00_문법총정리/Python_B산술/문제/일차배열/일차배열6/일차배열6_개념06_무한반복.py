'''
    [문제]
        [조건1] 리스트에 랜덤숫자(1~100) 5개를 추가한다.
        [조건2] 랜덤으로 홀수만 저장한다.   
'''
'''
    문제만 보면 5번 반복하면 될 것 같지만 함정이다. 
    홀수만 저장이기 때문에 무한반복을 사용해야 한다.
'''
import random

a = []

count = 0
while True :
    num = random.randint(1,100)
    if num % 2 == 1 :
        a.append(num)
        count += 1
    if count == 5 :
        break
    
print(a)