'''
	[문제]
		위 데이터는 학생 4명의 데이터이다.
		순서대로 [번호], [국어], [수학], [영어], [등수]의 데이터이다. 		
		이제 등수를 넣어야한다. 각 과목별 등수별로 점수를 매기고 
		각 점수들의 합이 가장적은 학생이 1등이다. 
		총합이 같으면 같은 등수이다. 

		1번학생은 국어 4등, 수학3등, 영어2등으로 점수는 9점이다. 
		2번학생은 국어 3등, 수학1등, 영어3등으로 점수는 7점이다.
		3번학생은 국어 2등, 수학4등, 영어1등으로 점수는 7점이다.
		4번학생은 국어 1등, 수학2등, 영어4등으로 점수는 7점이다.

		1등은 3명, 4등은 1명이다. 
	[정답]
		[1001, 20, 43, 54, 4],
		[1002, 21, 73, 44, 1],
		[1003, 65, 13, 55, 1],
		[1004, 76, 63,  4, 1]
'''
score = [
			[1001, 20, 43, 54, 0],
			[1002, 21, 73, 44, 0],
			[1003, 65, 13, 55, 0],
			[1004, 76, 63,  4, 0]
		]

# 각 과목별 점수만 배열에 담고
onlyScoreList = []
for i in range(3):
    onlyScoreList.append([])
    for j in range(4):
        onlyScoreList[i].append(score[j][i+1])

print(onlyScoreList)

# 각 과목별 등수를 담고
scoreLank = []
for i in range(len(onlyScoreList)):
	scoreLank.append([])
	for j in range(len(onlyScoreList[i])):
		scoreLank[i].append(1)
		for p in range(len(onlyScoreList[i])):
			if onlyScoreList[i][j] < onlyScoreList[i][p] :
				scoreLank[i][j] += 1

print(scoreLank)

# 학생별 점수 계산
totalScoreList = []
for i in range(len(scoreLank[0])):
	점수 = 0
	for j in range(len(scoreLank)):
		점수 += scoreLank[j][i]
	totalScoreList.append(점수)

print(totalScoreList)

# 점수에 따른 등수 계산
for i in range(len(totalScoreList)):
    count = 4
    for j in range(len(totalScoreList)):
        if totalScoreList[i] < totalScoreList[j]:
            count -= 1
    if totalScoreList[i] == min(totalScoreList):
        count = 1
    score[i][len(score[0])-1] = count
    print(score[i])
    

    
    
    
'''
for i in range(len(score)):
    점수.append(count)    
'''