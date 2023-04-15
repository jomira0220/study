'''
	[문제]
		a리스트에 랜덤(1~4) 숫자 4개를 저장한다. 
		단, 중복없는 숫자로 저장한다.
	
	[예시]
		[1,4,2,3]
'''
import random

a = []


while True :
    num = random.randint(1,4)
    check = True
    for i in range(len(a)) :
        if num == a[i] :
            check = False
            break
    if check :
        a.append(num)
    if len(a) == 4 :
        break
    
print(a)
            
    
    
