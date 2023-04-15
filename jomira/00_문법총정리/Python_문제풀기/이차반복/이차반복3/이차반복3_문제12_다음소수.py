'''
	[문제]
		2~1000 사이의 랜덤 숫자 하나를 저장한다.
		위 숫자 바로 다음 소수를 출력하시오.
	
	[예시1]
		r = 1000
		소수 = 1009	 
	[예시2]
		r = 500
	    소수 = 503
'''

import random
r = random.randint(2,1000)
# r = 500
소수 = r + 1

while True :
    count = 0
    for i in range(1,소수+1) :
        if 소수 % i == 0 :
            count += 1
            
    if count == 2 :
        print(f'r = {r}')
        print(f'소수 = {소수}')
        break
    else :
        소수 += 1
        

    