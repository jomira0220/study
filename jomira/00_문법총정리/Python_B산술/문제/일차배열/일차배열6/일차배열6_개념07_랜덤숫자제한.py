'''
	[문제] 
		a리스트 안에 1 또는 7을 랜덤으로 7개 추가 후 출력하시오. 
		단, 1의 개수는 4개만 추가하고,
		7의 개수는 3개만 추가한다.
		
	[예시]
		정답 [ 1, 7, 7, 1, 1, 7, 1]  # 개수가 맞다. 
		오답 [ 7, 1, 1, 7, 1, 1, 1]  # 7이 두개이다.
			
'''
import random

a = []

count7 = 0
count1 = 0

for i in range(7) :
    num = random.randint(1,2)
    
    if num == 2 :
        num = 7   
        
    if num == 2 and count7 < 3:
        count7 += 1
    if num == 1 and count1 < 4:
        count1 += 1
    
    a.append(num)
    

print(a)