'''
	[문제]		
		[1] com리스트에 0~9사이의 랜덤 숫자 3개를 저장하되 중복 값이 없어야 한다.
		[2] me리스트에 0~9사이의 랜덤 숫자 3개를 저장하되 중복 값이 없어야 한다.
		[3] com과 me 를 비교해서 숫자가 같고 자리도 같으면 strike + 1
		[4] com과 me 를 비교해서 숫자가 같고 자리가 틀리면 ball + 1
		[5] 사용자에게 strike와 ball 개수를 출력해 보여준다.
		
		계속 반복하면서 strike가 3이 되면 종료한다.
'''
import random
com = [0, 0, 0]
me = [0, 0, 0]

def randomList(com) :
    count = 0
    while True :
        num1 = random.randint(0,9)
        check = True
        for i in com :
            if num1 == i :
                check = False
        if check :
            com[count] = num1
            count += 1
        if count == 3 :
            break
        
randomList(com)
print(f'com ={com}')

while True :
    
    strike = 0
    ball = 0
    
    randomList(me)
    print(f'me ={me}')

    for i in range(len(com)):
        for j in range(len(me)) :
            if com[i] == me[j] :
                if i == j :
                    strike += 1
                else :
                    ball += 1
    
    print(f'strike = {strike}',end=' ')
    print(f'ball = {ball}')
    
    if strike == 3 :
        break
                
    
        
    
