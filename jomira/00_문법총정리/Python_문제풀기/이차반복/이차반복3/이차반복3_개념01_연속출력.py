'''
	[문제] 
		1~10 사이의 랜덤 숫자를 다섯 번 반복해서 저장하고, 
		랜덤 숫자 개수만큼 출력하시오.
	
 	[예시]
		예를 들어 4, 5, 3, 1, 2 가 나왔다고 한다면,
  
		4444
		55555
		333
		1
		22
'''

import random

a = []
for i in range(5) :
    a.append(random.randint(1,10))
    
print(f'a = {a}')

for i in range(len(a)) :
    for j in range(a[i]) :
        print(a[i], end='')
    print()
        

