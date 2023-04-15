'''
	[문제] 
		a리스트 안에 1 또는 7을 랜덤으로 7개 추가 후 출력하시오. 
		단, 7의 개수는 3개만 추가하고, 1의 개수는 4개만 추가한다.
		위에서 만든 복권을 판정한다. 
  		7이 연속으로 3개면 "당첨"을 출력한다.
		아니면 "꽝"을 출력한다.
		
	[예]
		[ 1, 7, 7, 1, 1, 7, 1]  "꽝"
		[ 1, 1, 1, 7, 7, 7, 1]  "당첨"
'''

import random
lotto = []

count7 = 0
count1 = 0 


while True :
    num = random.randint(1,2)
    if num == 2 :
        num = 7
    
    if num == 7 and count7 < 3 :
        count7 += 1
        lotto.append(num)  
    if num == 1 and count1 < 4 :
        count1 += 1
        lotto.append(num)
        
    if len(lotto) == 7 :
        break
        
count = 0
for num in lotto :
    if num == 7 :
        count += 1
        if count == 3 :
            break
    else :
        count = 0


if count == 3 :
    print(f'[{lotto}] 당첨')
else :
    print(f'[{lotto}] 꽝')