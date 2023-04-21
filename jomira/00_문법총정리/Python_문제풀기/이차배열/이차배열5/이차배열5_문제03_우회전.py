'''
    [문제]
        랜덤(1~4)를 저장한다. 랜덤숫자는 회전 횟수이다. 
        회전 횟수만큼 block의 숫자들을 90도로 우회전시키시오.
        
    [예시]
        rNum = 4
        1 2 3 
        4 5 6 
        7 8 9 

        7 4 1 
        8 5 2 
        9 6 3 

        9 8 7 
        6 5 4 
        3 2 1 

        3 6 9 
        2 5 8 
        1 4 7 
'''
block = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# x = 0 y = 0 0 
# x = 2 y = 0 1
# x = 2 y = 2 2
# x = 0 y = 2 3


import random 
rNum = random.randint(1,4)
rNum = 4
print('rNum = {}'.format(rNum))

for i in range(rNum):
    for j in range(3):
        print(block[j])
    print()

    temp1 = []
    print('temp1 = ')
    for j in range(3):
        temp2 = []
        for k in range(3):
            temp2.append(block[j][k])
        temp1.append(temp2)
        print(temp1[j])
    print()
    for j in range(3):
        for k in range(3):
            block[k][2-j] = temp1[j][k]