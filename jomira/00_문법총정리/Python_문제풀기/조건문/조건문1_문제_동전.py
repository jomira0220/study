'''
    [문제]
        동전의 앞과 뒤를 랜덤숫자 0 또는 1로 표현한다.
        동전 두 개를 던져서 둘 다 "앞"이면 "정답",
        둘 다 "뒤"이어도 "정답"이다.
        둘 중 하나라도 반대면 "꽝"을 출력하시오.
'''

import random
동전1 = random.randint(0,1)
동전2 = random.randint(0,1)

print(동전1,동전2)

if 동전1 == 동전2 : 
    print('정답')
else :
    print('꽝')    
