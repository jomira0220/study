'''
	[문제]
		a리스트는 학생 번호와 점수 한 세트를 이루고 있다.		
		일등 학생의 번호와 점수를 출력하시오.
	[정답]
		번호 = 1002
		점수 = 82
'''
a = [1001, 40, 1002, 82, 1003, 65, 1004, 70]

maxNum = 0
maxIndex = 0
for i in range(len(a)):
    if i % 2 == 1:
        if maxNum < a[i] :
            maxNum = a[i]
            maxIndex = i

print(f'번호 = {a[maxIndex-1]}')
print(f'점수 = {a[maxIndex]}')
        