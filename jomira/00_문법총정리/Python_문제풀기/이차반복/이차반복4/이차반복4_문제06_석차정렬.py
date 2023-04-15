'''
	[문제]
		석차를 출력하시오.
	[정답]
		2 3 4 1 
'''

numList = [1001, 1002, 1003, 1004]
scoreList = [87, 42,  11, 98]

# 방법 1
sortList = sorted(scoreList,reverse=True)
for i in range(len(scoreList)) :
    for j in range(len(sortList)) :
        if sortList[j] == scoreList[i] :
            print(j+1,end=' ')
            
            
# 방법 2           
for i in range(len(scoreList)):
	count = 0
	for j in range(len(scoreList)):
		if scoreList[i] <= scoreList[j]:
			count += 1
	print(count, end=" ")