'''
	[문제]
		[1] 1~9 사이의 랜덤 숫자 다섯개의 합을 total에 추가한다. 
		[2] 위 내용을 10번 반복하시오.
	[예시]
		7 2 8 4 5  : 26
		2 6 2 6 8  : 24
		4 6 7 1 5  : 23
		1 9 8 6 9  : 33
		6 1 3 1 2  : 13
		4 3 7 5 2  : 21
		6 2 7 9 3  : 27
		5 1 4 4 3  : 17
		1 3 9 4 6  : 23
		8 3 4 9 5  : 29
		total = [26, 24, 23, 33, 13, 21, 27, 17, 23, 29]
'''
import random

total = []

for i in range(10) :
    totalNum = 0
    for j in range(5) :
        num = random.randint(1,9)
        print(num, end=' ')
        totalNum += num
    print(f': {totalNum}')
    total.append(totalNum)

print(f'total = {total}')