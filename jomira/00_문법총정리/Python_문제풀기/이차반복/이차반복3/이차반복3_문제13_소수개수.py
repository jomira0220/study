'''
	[문제]
		2~100 사이의 랜덤 숫자 하나를 저장하고, 
		2부터 그 숫자 사이의 모든 소수의 개수를 출력하시오.

	[예시]
		r = 20
        소수 = 2, 3, 5, 7, 11, 13, 17, 19
		개수 = 8
'''
import random

r = random.randint(2,100)
print(f'r = {r}')

소수 = []
for i in range(2,r+1) : # 2이상부터 r이하까지
    count = 0
    for j in range(1,i+1) : #1이상부터 r이하까지
        if i % j == 0 :
            count += 1
    
    if count == 2 :
        소수.append(i)
        
print(f'소수 = {소수}')
print(len(소수))