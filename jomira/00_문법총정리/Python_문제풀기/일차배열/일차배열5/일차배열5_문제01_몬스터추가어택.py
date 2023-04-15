'''
    [문제]
        철수는 게임을 하고 있다. 
        monster는 게임의 적 4마리를 의미하고 9는 몬스터의 체력을 의미한다.
        철수의 공격력은 5이다.     
        랜덤으로 몬스터 중 하나를 선택해서 공격하고,
        이를 총 다섯 번 반복한다. 
        모든 몬스터를 공격한 후 몬스터들의 체력을 출력하시오.
        단, 몬스터 체력은 0이 되면 더 이상 내려가지 않는다. 
        또한 공격한 몬스터의 양쪽에게는 1의 대미지를 가하게 된다. 
        
'''

import random

monster = [9,7,8,6]
power = 5


for i in range(5) :
    
    attackIndex = random.randint(0,len(monster)-1)
    
    if monster[attackIndex] >= 0 :
        
        if monster[attackIndex] - power > 0:
            monster[attackIndex] -= power
        
        #공격한 몬스터 앞 몬스터의 인덱스가 4보다 크면
        if attackIndex+1 > len(monster)-1:
            #첫번째 몬스터의 값이 0보다 크면 차감하고
            #0보다 작으면 0처리
            if monster[0] > 0:
                monster[0] -= 1
            else :
                monster[0] = 0
        else :
            if monster[attackIndex+1] > 0 :
                monster[attackIndex+1] -= 1
            else :
                monster[attackIndex+1] = 0

        #공격한 몬스터 뒤 몬스터의 인덱스가 0보다 작으면
        if attackIndex-1 < 0:
            #마지막 몬스터의 값이 0보다 크면 차감하고
            #0보다 작으면 0처리
            if monster[len(monster)-1] > 0: 
                monster[len(monster)-1] -= 1
            else :
                monster[len(monster)-1] = 0
        else :
            if monster[attackIndex-1] > 0:
                monster[attackIndex-1] -= 1
            else :
                monster[attackIndex-1] = 0
        
        
        if monster[attackIndex] == 0:
            print("체력이 0인", end=' ')
            
    else :
        monster[attackIndex] = 0
        
    print(f'{attackIndex}번째 몬스터 공격! ==> {monster}')
    