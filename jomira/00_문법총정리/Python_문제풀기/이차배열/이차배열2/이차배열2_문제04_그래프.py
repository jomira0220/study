'''
    [문제]
         a이차리스트에 data의 값들만큼 1을 채워 넣으시오.
         단, 가로를 기준으로 왼쪽에서 오른쪽으로 저장하시오.
         결과를 사각형 모양으로 출력하시오.
    [정답]
        [1,1,1,1,1,0,0,0,0,0]
        [1,1,1,0,0,0,0,0,0,0]
        [1,1,1,1,1,1,1,0,0,0]
        [1,1,1,0,0,0,0,0,0,0]
        [1,1,1,1,1,1,1,1,1,0]
         
'''
data = [5,3,7,3,9]
a = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

for i in range(len(a)) :
    for j in range(data[i]) :
        a[i][j] = 1
    print(a[i])