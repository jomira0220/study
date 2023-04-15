'''
    [문제]
        a리스트에는 이미 1~3의 값이 저장되어 있다.
        이제 추가로 랜덤(1~10)을 10번 추가하려 한다. 
        단, 중복숫자가 있으면 저장하지 않는다.
    [예시]
        [1, 2, 3, 10, 8, 9, 4]
'''
import random

a = [1,2,3]

for i in range(10) :
    num = random.randint(1,10)
    check = True
    for i in a :
        if i == num :
            check = False
            break 
    if check :
        a.append(num)
        
print(a)

'''
# 중복되지 않게 랜덤 숫자 10개 저장
while True :
    num = random.randint(1,10)
    check = True
    for i in a :
        if i == num :
            check = False
            break 
    if check :
        a.append(num)

    if len(a) == 10 : break
    
print(a)
'''