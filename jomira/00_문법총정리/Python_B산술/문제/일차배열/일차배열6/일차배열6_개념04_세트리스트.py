'''
	[문제]
		a리스트는 학생 번호와 점수가
		한 세트를 이루고 있다.
		점수 총합과 평균을 출력하시오.
	[정답]
		총점 = 235
		평균 = 58.75
'''
#           1         3         5         7
a = [1001, 40, 1002, 60, 1003, 65, 1004, 70]

total = 0
count = 0
for i in a :
    if a.index(i) % 2 == 1 :
        total += i
        count += 1
        
print(total)
print(total / count)