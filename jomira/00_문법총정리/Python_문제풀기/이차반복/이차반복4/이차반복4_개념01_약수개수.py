'''
	[문제]
		a리스트의 각 값의 약수를 전부 출력하고 
		각 약수의 개수를 count리스트에 추가하시오.

	[예시]
		1 43 
		1 5 11 55 
		1 5 13 65 
		1 11 		
		count = [2, 4, 4, 2]
	
	[정답]
		count = [2, 4, 4, 2]
'''

a = [43,55,65,11]
count = []

for i in a :
    cnt = 0
    for j in range(1,i+1) :
        if i % j == 0 :
            cnt += 1
    count.append(cnt)

print(count)