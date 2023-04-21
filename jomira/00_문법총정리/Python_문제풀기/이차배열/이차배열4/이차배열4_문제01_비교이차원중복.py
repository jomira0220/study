'''
    [문제]
        a리스트와 b리스트를 비교해서 
        서로 겹치는 값을 0으로 변경하시오.
        중복되는 값은 전부 0으로 변경한다.
    [정답]
    a = [
            [0, 4, 0],
            [0, 0, 0],
            [0, 4, 0]
        ]
    b = [
            [0, 0, 0],
            [0, 0, 8],
            [6, 0, 0]
        ]
'''

a = [[1,4,3],[5,7,2],[5,4,1]]
b = [[5,3,2],[1,7,8],[6,5,1]]
check = []
for i in range(len(a)) :
    for j in range(3) :
        for p in range(len(b)) :
            for k in range(3) :
                if a[i][j] == b[p][k] :
                    b[p][k] = 0
                    check.append(a[i][j])
        

for i in range(len(a)) :
    for j in range(3) :                
        for o in range(len(check)):
            if check[o] == a[i][j] :
                a[i][j] = 0     

            
print("a={}".format(a))
print("b={}".format(b))