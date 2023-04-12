'''
	[문제]
		다음은 학생 번호와 점수의 한 세트이다.
		일등의 번호와 점수, 꼴등의 번호와 점수를 출력하시오.
	[정답]
		일등 = 1004 98
		꼴등 = 1002 11
'''


numberList = [1001, 1002, 1003, 1004, 1005]
scoreList = [87, 11, 45, 98, 23]


maxScore = max(scoreList)
minScore = min(scoreList)

for index,score in enumerate(scoreList) :
    if score == maxScore :
        print(f'일등 = {numberList[index]}, {maxScore}점')
    if score == minScore :
        print(f'꼴등 = {numberList[index]}, {minScore}점') 