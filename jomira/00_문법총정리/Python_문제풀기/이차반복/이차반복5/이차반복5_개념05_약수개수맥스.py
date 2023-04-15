'''
	[문제]
		a리스트의 각 값의 약수들을 전부 출력하고 
		각 약수의 개수를 count리스트에 추가한다.

		개수가 가장 많은 약수를 max리스트에 추가한다. 
		개수가 가장 많은 약수가 여러 개일 땐 전부 추가한다. 
	[예시]
		1 43 
		1 5 11 55 
		1 5 13 65 
		1 11 		
		count = [2, 4, 4, 2]
		max = [55, 65]
	[정답]
		max = [55, 65]
'''
a = [43,55,65,11]
countList = []
maxNumList = []

for i in range(len(a)) :
    cnt = 0
    for j in range(1,a[i]+1) :
        if a[i] % j == 0 :
            print(j,end=' ')
            cnt += 1
    countList.append(cnt)
    print()

print(f'count = {countList}')

maxNum = max(countList)
for i in range(len(countList)) :
    if countList[i] == maxNum :
        maxNumList.append(a[i])
print(f'maxNumList = {maxNumList}')

    