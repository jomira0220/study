'''
    [문제]
         a이차리스트에 10~90까지 값을 저장 후 셔플하시오.
    [예시]
        셔플 전 >>>
        [10, 20, 30]
        [40, 50, 60]
        [70, 80, 90]
        
        셔플 후 >>> 
        [40, 20, 80]
        [10, 60, 90]
        [30, 70, 50]    
'''
import random

a = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

b = [10,20,30,40,50,60,70,80,90]

index = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = b[index]
        index += 1
        
for i in range(len(a)):
    
    r1 = random.randint(0, len(a)-1)
    r2 = random.randint(0, len(a)-1)
    temp = a[r1][r2]
    a[r1][r2] = a[0][0]
    a[0][0] = temp
    
    print(a[i])
    