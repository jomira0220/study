student = [
			["번호",  "이름",  "성별"],
			[1001,  "이만수",  "남" ],
			[1002,  "이영희",  "여" ],
			[1003,  "김민정",  "여" ],
			[1004,  "이철민",  "남" ],
			[1005,  "오만석",  "남" ],
			[1006,  "최이슬",  "여" ]
		]
		
score = [
			["번호", "국어", "수학"],
			[1001,      10,     20],
			[1002,      70,     30],
			[1003,      64,     65],
			[1004,      13,     87],
			[1005,      49,     80],
			[1006,      14,     90]
		]
'''
	[문제1] 
		여학생들 점수 총합과 남학생들의 점수 총합을 비교하고
		점수가 더 큰쪽을 출력하시오.
	[정답1]
		333
'''
man = 0
women = 0
for i in range(1,len(student)):
    total = score[i][1] + score[i][2]
    if student[i][2] == "남":
        man += total
    else :
        women += total
        
if man < women :
    print(women)
else :
    print(man)

'''
	[문제2]
		평균이 60점이상이면 합격이다.
		합격생들 번호, 이름, 평균을 출력하시오.
	[정답2]
		1003 김민정 64.5
		1005 오만석 64.5
'''
for i in range(1,len(score)):
    total = score[i][1] + score[i][2]
    avg = total / 2
    if avg >= 60 :
        print(student[i][0],student[i][1],round(avg,1))


'''
	[문제3]
		국어점수가 수학점수 보다 큰 학생들 
		번호, 이름을 출력하시오.
	[정답3]
		1002 이영희
'''
for i in range(1,len(score)):
    if score[i][1] > score[i][2] :
        print(student[i][0],student[i][1])



'''
	[문제4]
		총점이 1등인 학생의 번호, 이름을 출력하시오.
		만약 여러명이면 전부 출력하시오.
	[정답4]
		1003 김민정
		1005 오만석
'''
maxScore = 0
for i in range(1,len(score)):
    total = score[i][1] + score[i][2]
    if total > maxScore:
        maxScore = total
        
for i in range(1,len(student)):
    total = score[i][1] + score[i][2]
    if maxScore == total:
        print(student[i][0],student[i][1])