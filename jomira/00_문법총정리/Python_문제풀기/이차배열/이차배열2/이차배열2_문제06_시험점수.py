'''
    student리스트는 이번 학기 중간고사 성적이다.
    가로 한 줄을 기준으로 맨 앞은 번호이고, 뒤에 숫자 3개는
    각각 국어, 수학, 영어 점수이다. 
'''
student = [
    [1001, 100, 20, 32],        # 152
    [1002, 40, 43, 12],         # 95
    [1003, 60, 21, 42],         # 123
    [1004, 76, 54, 55],         # 185
    [1005, 23, 11, 76],         # 110
]
rank = [0,0,0,0,0]

'''
    [문제1] 
        모든 점수의 총합을 출력하시오.
    [정답1] 
        665
'''
print("[문제1]")
total = 0
for i in range(len(student)) :
        total += student[i][1] + student[i][2] + student[i][3]
print(total)


'''
    [문제2] 
        국어 1등 번호를 출력하시오.
    [정답2]         	
        1001
'''
print("[문제2]")
maxScore = 0
maxIndex = 0
for i in range(len(student)) :
    if student[i][1] > maxScore :
        maxScore = student[i][1]
        maxIndex = i

print(student[maxIndex][0])
        

'''
    [문제3] 
        수학 1등 번호를 출력하시오.
    [정답3]    
        1004    
'''
print("[문제3]")
maxScore = 0
maxIndex = 0
for i in range(len(student)) :
    if student[i][2] > maxScore :
        maxScore = student[i][2]
        maxIndex = i
print(student[maxIndex][0])



'''        	
    [문제4] 
        영어 1등 번호를 출력하시오.
    [정답4]
        1005
'''
print("[문제4]")
maxScore = 0
maxIndex = 0
for i in range(len(student)) :
    if student[i][3] > maxScore :
        maxScore = student[i][3]
        maxIndex = i
print(student[maxIndex][0])



'''
    [문제5] 
        전체 1등 번호를 출력하시오.
    [정답5]
        1004
'''
print("[문제5]")
totalScore = [] # 학생별 점수합
for i in range(len(student)) :
    totalScore.append(student[i][1] + student[i][2] + student[i][3])
    
maxTotalScore = 0
maxTotalIndex = 0
for i in range(len(totalScore)) :
    if maxTotalScore < totalScore[i] :
        maxTotalScore = totalScore[i]
        maxTotalIndex = i
print(student[maxTotalIndex][0])
    
    


'''
    [문제6] 
        수학점수가 국어점수 보다 높은 번호를 출력하시오.
    [정답6]
        1002
'''
print("[문제6]")

for i in range(len(student)) :
    if student[i][1] < student[i][2] :
        print(student[i][0])



'''
    [문제7]
        세 과목의 총합의 등수를 rank리스트에 저장하시오.
    [정답7]
        [2, 5, 3, 1, 4]
'''
print("[문제7]")

for i in range(len(totalScore)) :
    count = 1
    for j in range(len(totalScore)) :
        if totalScore[i] < totalScore[j] :
            count += 1
    rank[i] = count
    
print(rank)