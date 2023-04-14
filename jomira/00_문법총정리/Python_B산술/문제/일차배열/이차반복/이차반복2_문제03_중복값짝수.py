'''
	[문제]
		a리스트와 b리스트를 전체 비교하여 
		a리스트 안에도 있고 b리스트 안에도 있는 값은 c리스트에 저장하시오. 
		단, 짝수만 저장하시오.
	[정답]
		[2, 6]
'''
a = [1, 2, 7, 40, 3, 6]
b = [1, 6, 2, 9, 3, 7]
c = []

size = len(a)

for i in range(len(a)):
	for j in range(len(b)):
		if a[i] == b[j] and a[i] % 2 == 0:
			c.append(a[i])
print(c)
'''
tempA = [] 
tempB = []

for i in range(size) :
    if a[i] % 2 == 0 :
        tempA.append(a[i])
    if b[i] % 2 == 0 :
        tempB.append(b[i])

tempA = list(set(tempA))
tempB = list(set(tempB))

for i in range(len(tempA)) :
    for j in range(len(tempB)) :
        if tempA[i] == tempB[j] :
            c.append(tempA[i])

print(c)
'''