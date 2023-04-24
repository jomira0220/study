'''
	[문제]
		세로 가로 인덱스 두 개를 랜덤으로 저장한다. 
		그 인덱스를 기점으로 대각선 방향으로 전부 1로 채운 후 출력하시오.
		    
		[예]
			y = 2
			x = 1
		    	
			[0,0,0,1,0]
			[1,0,1,0,0]
			[0,1,0,0,0]
			[1,0,1,0,0]
			[0,0,0,1,0]
'''
list = [
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0]
]

import random
y = random.randint(0,len(list)-1)
x = random.randint(0,len(list[0])-1)

print('y = {}, x = {}'.format(y,x))

# x += 1 y -= 1 오른쪽 위대각선 
# x -= 1 y += 1 왼쪽 아래대각선 
# x += 1 y += 1 오른쪽 아래대각선 
# x -= 1 y -= 1 왼쪽 아래대각선
size = len(list)
i = 0
while i <= 5 :
    check = True
    if x+1 < size and y-1 >= 0:
        list[y-1][x+1] = 1
        check = False
    if x-1 >= 0 and y+1 < size:
        list[y+1][x-1] = 1
        check = False
    if x+1 < size and y+1 < size:
        list[y+1][x+1] = 1
        check = False
    if x-1 >= 0 and y-1 >= 0:
        list[y-1][x-1] = 1
        check = False
    
    if check : break
    i += 1
    
    
for i in range(len(list)):
    print(list[i])
