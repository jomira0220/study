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
print('size = {}'.format(size))

list[y][x] = 1
tempY = y
tempX = x

while True :
    if x + 1 < size and y - 1 >= 0 :
        x += 1
        y -= 1
        list[y][x] = 1
    else:
        break

y = tempY
x = tempX
while True :
    if x + 1 < size and y + 1 < size :
        x += 1
        y += 1
        list[y][x] = 1
    else:
        break
    
y = tempY
x = tempX
while True :
    if x - 1 >= 0 and y + 1 < size :
        x -= 1
        y += 1
        list[y][x] = 1
    else:
        break
    
y = tempY
x = tempX
while True :
    if x - 1 >= 0 and y - 1 >= 0 :
        x -= 1
        y -= 1
        list[y][x] = 1
    else:
        break


for i in range(len(list)) :
    print(list[i])