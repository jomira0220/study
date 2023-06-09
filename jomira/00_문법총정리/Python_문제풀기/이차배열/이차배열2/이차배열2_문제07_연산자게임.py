'''
    [문제]
        game 리스트의 각 가로줄은 한게임을 뜻한다. 
        첫 번째 숫자와 두 번째 숫자를 더하거나 빼거나 곱해서
        그 결과를 total에 저장하면 된다.
        
        더하거나 빼거나 곱하는 기준은 각 가로의 마지막 숫자로 판별한다.
        0이면 더하기
        1이면 빼기
        2면 곱하기이다. 
        
        위 내용을 한줄씩 내려오면 5번 반복하시오.
    [예시]
        [5,9,0] : 은 5 + 9 이다 total = [14]
        [3,7,1] : 은 3 - 7 이다 total = [14, -4]
        [8,4,2] : 는 8 * 4 이다 total = [14, -4, 32]
        ...
        ...
    [정답]
        [14, -4, 32, 18, -2]
'''
game = [
    [5,9,0],
    [3,7,1],
    [8,4,2],
    [9,2,2],
    [4,6,1],
]
total = []


for i in range(len(game)) :
    if game[i][2] == 0 :
        total.append(game[i][0] + game[i][1])
    elif game[i][2] == 1 :
        total.append(game[i][0] - game[i][1])
    elif game[i][2] == 2 :
        total.append(game[i][0] * game[i][1])


print(total)