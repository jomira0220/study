'''
    [문제]
        철수는 빙고 게임을 만들고 있다.
        빙고 조건은 가로 1이 3개 또는 세로 1이 3개 또는 대각선으로 1이 3개이면 빙고이다.
        빙고는 중첩될 수 있다.
        반복적으로 랜덤 위치에 1을 저장한다. 
        단, 한번 1이 저장된 곳은 또 다시 저장할 수 없다.
        3빙고가 성립되면 종료한다. 
'''
bingo = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

import random


while True :
    y = random.randint(0,2)
    x = random.randint(0,2)
    
    if bingo[y][x] == 0 :
        bingo[y][x] = 1
    else:
        continue
    
    bingoCount = 0
    for i in range(len(bingo)) :
        widthCount = 0
        lengthCount = 0
        for j in range(len(bingo[i])) :
            if bingo[i][j] == 1 :
                widthCount += 1
                if widthCount % 3 == 0 :
                    bingoCount += 1
                    
            if bingo[j][i] == 1 :
                lengthCount += 1
                if lengthCount % 3 == 0 :
                    bingoCount += 1
                    
        
        if bingo[0][0] == 1 and bingo[1][1] == 1 and bingo[2][2] == 1 :
            bingoCount += 1
        if bingo[0][2] == 1 and bingo[1][1] == 1 and bingo[2][0] == 1 :
            bingoCount += 1
    for b in range(len(bingo)) :
        print(bingo[b])        
    print()
    if bingoCount >= 3 :
        break

        
        
        

