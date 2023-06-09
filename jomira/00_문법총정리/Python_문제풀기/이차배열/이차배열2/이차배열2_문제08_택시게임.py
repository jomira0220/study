'''
    [문제]
        현재 택시는 5, 5 위치에 있다.
        배열의 왼쪽 세로줄은 속도를 뜻한다.
        배열의 오른쪽 세로줄은 방향 뜻하고 
        (0, 1, 2, 3)은 (북, 동, 남, 서)를 뜻한다. 
        속도와 방향은 택시가 매번 이동한 내용을 기록한 것이다.
        6번 모두 이동한 후 택시의 최종위치를 출력하시오.  
    [예시] 
        [4,0] 
            속도는 4이고 방향은 0이니 북쪽을 뜻한다. 
            y가 4증가해  x : 5, y : 9 가 된다.  
    [정답]  
        x = 8 y = 0
'''
game = [
    [4,0],      
    [2,1],
    [1,3],
    [5,2],
    [4,2],
    [2,1]
]
x = 5
y = 5


for i in range(len(game)) :
    if game[i][1] == 1 :
        x += game[i][0]
    elif game[i][1] == 3 :
        x -= game[i][0]
    elif game[i][1] == 2 :
        y -= game[i][0]
    elif game[i][1] == 0 :
        y += game[i][0]
        
    print(f'x = {x}, y = {y}')