'''
	[문제]
		[1] a리스트에 1~10까지의 랜덤 숫자 3개를 저장 후 출력하시오.
		[2] 단, 숫자 3개는 서로 중복되면 안 된다. 
		[3] 숫자 3개의 합은 반드시 20이어야 한다. 
	[예시]
		[3, 10, 7] o 
		[5, 10, 5] x 
'''

import random

a = [0,0,0]
count = 0
while True :
    num = random.randint(1,10)
    check = True
    for i in a :
        if i == num :
            check = False
            break
    if check :
        a[count] = num
    
    if count == 2 :
        if sum(a) == 20 : 
            print(f'{a} O') 
            break
        else :
            print(f'{a} X')
            count = 0
            continue
        
    count += 1  
    
    
    

    


