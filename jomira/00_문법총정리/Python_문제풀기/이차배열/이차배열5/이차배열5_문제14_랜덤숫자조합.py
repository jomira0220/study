'''
	[문제]
		철수는 게임을 만들려고 한다.
		숫자 다섯 개를 랜덤(1~9사이의 숫자)으로 저장한다.
		각각의 숫자는 중복이 되면 안된다.

		각각의 숫자로 랜덤 조합을 4가지 만들어서
		numList에 저장하고, 전체 합을 출력하시오.
		랜덤 조합 역시 중복이 되면 안된다.
		[예]
			1, 3, 5, 7, 9 라고 했을 때
			[1] 13597
			[2] 51397
			[3] 37951
			[4] 91537

			정답 : 13597 + 51397 + 37951 + 91537 = 194482
'''
import random
numList = []

numList.append('')
for i in range(5):
    num = random.randint(0,9)
    numList[0] += str(num)

start = 1
for j in range(1,len(numList[0])-1):
    numList.append('')
    for i in range(len(numList[0])):
        numList[j] += numList[0][start]
        start += 1 
        start %= 5 
    start += 1

    
for i in range(len(numList)):
    print(numList[i])

numList = list(map(int,numList))
print(numList)
print(sum(numList))
    
    