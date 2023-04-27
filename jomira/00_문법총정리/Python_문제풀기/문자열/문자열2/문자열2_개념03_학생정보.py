student = [
		["번호",  "이름", "성별", "국어", "수학"],
		[1001, 	"이만수",  "남",     10,     20],
		[1002,  "이영희",  "여",     70,     30],
		[1003,  "김민정",  "여",     64,     65],
		[1004,  "이철민",  "남",     13,     87],
		[1005,  "오만석",  "남",     49,     80],
		[1005,  "최이슬",  "여",     14,     90]
	]

'''
	[문제1] 
		여학생들 점수 총합과 남학생들의 점수 총합을 비교하고
		점수가 더 큰 쪽을 출력하시오.
	[정답1]
		333
'''
print("[문제1]")
woman = 0
men = 0
for i in range(1,len(student)):
    if student[i][2] == "여":
        woman += student[i][3] + student[i][4]
    else : 
        men += student[i][3] + student[i][4]    

if woman > men :
    print(woman)
else :
    print(men)


'''
	[문제2] 
		평균이 60점 이상이면 합격이다.
		합격생들 번호, 이름, 평균점수를 출력하시오.
	[정답2]
		1003 김민정 64.5
		1005 오만석 64.5
'''
print("[문제2]")
for i in range(1,len(student)):
    totalScore = student[i][3] + student[i][4]
    avg = totalScore / 2
    if avg >= 60 :
        print(student[i][0],student[i][1],round(avg,1))   
    

'''
	[문제3] 
		국어 점수가 수학 점수 보다 큰 학생들의
		번호, 이름을 출력하시오.
	[정답3]
		1002 이영희
'''
print("[문제3]")

for i in range(1,len(student)):
    if student[i][3] > student[i][4]:
        print(student[i][0],student[i][1])


'''
	[문제4] 
		1등의 번호, 이름을 출력하시오.
		만약 여러 명이면 전부 출력하시오.
	[정답4]
		1003 김민정
		1005 오만석
'''
print("[문제4]")
max = 0
for i in range(1,len(student)):
    total = student[i][3] + student[i][4]
    if total > max :
        max = total
        
for i in range(1,len(student)):
    total = student[i][3] + student[i][4]
    if max == total :
        print(student[i][0],student[i][1])
    