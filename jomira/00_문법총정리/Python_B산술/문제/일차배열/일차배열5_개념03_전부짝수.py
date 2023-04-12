'''
	[문제]
		a리스트에 랜덤(0~9) 사이의 랜덤 값을 4개 저장한 후 출력한다. 
		리스트 안의 값들이 모두 짝수면 True를 출력하고,
		하나라도 짝수가 아니면 False를 출력한다.
		단, 0은 짝수이다.
	[예시] 
		[4, 6, 2, 0] True
		[5, 2, 0, 4] False
'''

import random

a = []
#[방법1]
count = 0
for i in range(4) :
    a.append(random.randint(0,9))
    if a[i] % 2 == 0 :
        count += 1
        
if count == len(a) : 
    print(f'{a} True')
else :
    print(f'{a} False')
    
    
#[방법2]
check = True

for i in range(len(a)):
	if a[i] % 2 == 1:
		check = False

print(check)
    
    
    
''' 
[중복없는 리스트 셋팅 방법]
run = 1
while run == 1 :
    a.append(random.randint(0,9))
    a = list(set(a))
    if len(a) == 4 :
        break

for i in a :
    if i % 2 == 0 :
        count += 1
        
if count == len(a) : 
    print(f'{a} True')
else :
    print(f'{a} False')
'''


