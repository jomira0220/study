'''
	[문제]
		철수는 철수의 마블 게임을 개발 중이다. 
		map1과 map2는 게임 스테이지를 표현한다. 
		숫자 1은 철수의 위치이다. 
		주사위는 1~6까지 있고 주사위 2개를 던저서 그 합만큼 앞으로 이동한다. 		
		map1의 끝에 도달하면 map2로 이동해서 전진하고, 
		map2의 끝에 도달하면 다시 map1로 이동해서 전진한다. 		
		주사위를 총 4번 반복하고 철수의 위치를 출력하시오.
	[예시]
	(1)	시작
		map1 = [1,0,0,0,0,0,0,0,0,0]
		map2 = [0,0,0,0,0,0,0,0,0,0]
  
	(2)	주사위 3 , 5 : 8
		map1 = [0,0,0,0,0,0,0,0,1,0]
		map2 = [0,0,0,0,0,0,0,0,0,0]
		
	(3)	주사위 2 , 1 : 3
		map1 = [0,0,0,0,0,0,0,0,0,0]
		map2 = [0,1,0,0,0,0,0,0,0,0]
		
	(4)	주사위 6 , 1 : 7
		map1 = [0,0,0,0,0,0,0,0,0,0]
		map2 = [0,0,0,0,0,0,0,0,1,0]
		
	(5)	주사위 3 , 3 : 6
		map1 = [0,0,0,0,1,0,0,0,0,0]
		map2 = [0,0,0,0,0,0,0,0,0,0]
			
'''

import random

map1 = [1,0,0,0,0,0,0,0,0,0]
map2 = [0,0,0,0,0,0,0,0,0,0]

print('시작')
print(f'map1 = {map1}')
print(f'map2 = {map2}')

position = 0
turn = True
size = len(map1)

for i in range(4) :
    
    #기존 position 1 없애기
    if turn :
        map1[position] = 0
    else :
        map2[position] = 0
    
    #주사위 랜덤값 및 주사위합
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    total = r1 + r2
    
    #주사위의 합이 현재 위치한 배열의 길이보다 클때는 배열 바꿈 
    position += total
    if position >= size :
        turn = not turn
        position %= size

    if turn :
        map1[position] = 1
    else :
        map2[position] = 1
    
    print()
    print(f'주사위 {r1},{r2} : {total} / position = {position}')
    print(f'map1 = {map1}')
    print(f'map2 = {map2}')




