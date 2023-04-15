'''
	[문제]
		a리스트와 b리스트를 비교하여 
		서로 겹치는 값을 0으로 변경하시오.
		겹치는 값이 여러 개면 전부 0으로 변경하시오.
	[정답]
		a = [0, 0, 30, 40, 0]
		b = [0, 3, 0, 0, 0, 50]
'''

a = [10,20,30,40,20]
b = [10,3,20,10,20,50]

for i in range(len(a)) :
    check = False
    for j in range(len(b)) :
        if a[i] == b[j] :
            b[j] = 0
            check = True
    
    if check :
        a[i] = 0

print(f'a = {a}')
print(f'b = {b}')