'''
[문제]
	[1] 1~99 사이의 랜덤 숫자를 저장한다.
	
	랜덤 숫자 중에서 3이나 6이나 9의 개수가
	[2-1] 2개이면, 짝짝을 출력한다.
	[2-2] 1개이면, 짝을 출력한다.
	[2-3] 0개이면, 해당 숫자를 출력하시오.
	
	[예]
		33	==> 짝짝
		16	==> 짝
		 7	==> 7
'''


import random
num = random.randint(1,99)
#num = 33
십의자리 = num // 10
일의자리 = num % 10

count = 0
if 일의자리 == 3 or 일의자리 == 6 or 일의자리 == 9 :
    count += 1
if 십의자리 == 3 or 십의자리 == 6 or 십의자리 == 9 :
    count += 1

if count == 1 :
    result = '짝'
elif count == 2 :
    result = '짝짝'
else :
    result = num

        
print(num, result)


    