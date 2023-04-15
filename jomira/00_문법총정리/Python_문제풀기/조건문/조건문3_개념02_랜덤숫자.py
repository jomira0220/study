'''
[문제]
    랜덤으로 숫자 1이나 7을 출력하시오.
'''
import random
num = random.randint(1,2)

if num == 2 :
    num = 7
    
print(num)