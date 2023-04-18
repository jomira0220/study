'''
    apt 리스트는 아파트 1동의 각 세대를 의미한다.
    pay 는 이번달 관리비를 뜻한다.
'''
import random

apt = [
		[101, 102, 103],	
		[201, 202, 203],	
		[301, 302, 303]		
	]		
pay = [
		[1000, 2100, 1300],	 
		[4100, 2000, 1000],	 
		[3000, 1600,  800]  
	]
rank = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

'''
    [문제 1] 
        각 층별 관리비 합을 출력하시오.
    [정답 1] 
        4400 7100 5400
'''
print("[문제1]")

for i in pay :
    print(sum(i), end='')
print()



'''
    [문제 2] 
        랜덤으로 호수와 관리비 한개 출력하시오.
    [예시 2]
        0 2
        103 1300 원 
'''
print("[문제2]")
y = random.randint(0,len(apt)-1)
x = random.randint(0,len(apt[0])-1)
print(y,x)
print(apt[y][x],pay[y][x])


'''
    [문제 3] 
        관리비가 가장 많이 나온 집, 가장 적게 나온 집을 출력하시오.
    [정답 3]
        가장 많이 나온 집 = 201
        가장 적게 나온 집 = 303    
'''
print("[문제3]")
maxNum = 0
maxIndex = []
for i in range(len(pay)) :
    for j in range(len(pay)) :
        if pay[i][j] > maxNum:
            maxNum = pay[i][j]
            maxIndex = [i,j]

print(f'가장 많이 나온 집 = {apt[maxIndex[0]][maxIndex[1]]}')

minNum = maxNum
minIndex = []
for i in range(len(pay)) :
    for j in range(len(pay)) :
        if pay[i][j] < minNum :
            minNum = pay[i][j]
            minIndex = [i,j]

print(f'가장 적게 나온 집 = {apt[minIndex[0]][minIndex[1]]}')

'''     
    [문제 4] 
        관리비 많이 나온 순서대로 rank 리스트에 등수를 저장하시오.
    [정답 4]
        [7, 3, 6]
        [1, 4, 7]
        [2, 5, 9]
'''
print("[문제4]")
temp = []
for i in range(len(pay)):
    for j in range(len(pay[i])):
        temp.append(pay[i][j])

print(f'temp = {temp}')

y = 0
x = 0
for i in range(len(temp)):
    count = 1
    for j in range(len(temp)):
        if temp[i] < temp[j]:
            count += 1
    
    rank[y % 3][x % 3] = count
    x += 1

    if i % 3 == 2:
        y += 1
    
for i in range(len(rank)):
    print(rank[i])
    

