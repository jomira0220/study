'''
    [문제]
        철수는 게임을 만들고 있다.
        game리스트는 이차원으로 되어있다.
        숫자8은 플레이어 위치를 뜻한다.
        숫자0은 플레이어가 움직일 수 있는 위치이다.
        
        order리스트는 플레이어가 움직이게 하는 명령어이다.
        1,2,3,4는 차례대로 북, 동, 남, 서를 뜻한다. 

        order의 이동대로 플레이어를 이동시키고 출력하시오.
        플레이어가 벽에 붙어서,
        더 이상 원하는 방향으로 이동할 수 없을 때는 "이동 불가"를 출력한다.
    [정답]        
        캐릭터의 현재 위치 = 2 , 2
        0 0 0 0 0
        0 0 0 0 0
        0 0 8 0 0
        0 0 0 0 0
        0 0 0 0 0 

        북
        0 0 0 0 0
        0 0 8 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0

        남
        0 0 0 0 0
        0 0 0 0 0
        0 0 8 0 0
        0 0 0 0 0
        0 0 0 0 0

        남
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 8 0 0
        0 0 0 0 0

        남
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 8 0 0

        서
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 8 0 0 0

        남
        이동 불가
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 8 0 0 0

        남
        이동 불가
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 8 0 0 0

        서
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        8 0 0 0 0

        동
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 8 0 0 0
'''

game = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,8,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

order = [1,3,3,3,4,3,3,4,2]

y = 0
x = 0

for i in range(len(game)) :
    for j in range(len(game)) :
        if game[i][j] == 8 :
            y = i
            x = j

print('y = {}'.format(y))
print('x = {}'.format(x))



for i in range(len(order)) :
    
    for g in range(len(game)) :
        print(game[g])
    print()
    
    tempY = y
    tempX = x
    
    print('y = {}, x = {}'.format(y,x))
    
    check = True
    if order[i] == 2 and x+1 < len(game[0]):
        x += 1
        print('동','y = {}, x = {}'.format(y,x))
    elif order[i] == 4 and x-1 >= 0:
        x -= 1
        print('서','y = {}, x = {}'.format(y,x))
    elif order[i] == 3 and y+1 < len(game):
        y += 1
        print('남','y = {}, x = {}'.format(y,x))
    elif order[i] == 1 and y-1 >= 0:
        y -= 1
        print('북','y = {}, x = {}'.format(y,x))
    else :
        check = False
    
    if check :
        game[y][x] = 8
        game[tempY][tempX] = 0
        tempY = y
        tempX = x
    else :
        print('이동불가')
    
        

for g in range(len(game)) :
    print(game[g])