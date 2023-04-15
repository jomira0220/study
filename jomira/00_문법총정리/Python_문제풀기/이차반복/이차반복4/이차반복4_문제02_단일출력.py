'''
	[문제]
		a리스트의 숫자를 하나씩 출력한다.
		단, 이미 출력이 되어 중복되는 숫자는 출력하지 마시오.
	[정답]
		1 2 3 4 100		
'''
a = [1,1,2,2,3,3,4,100,3]

# 방법 1
a = sorted(list(set(a)))
print(a)


# 방법 2
for i in range(len(a)) :
    check = True
    for j in range(i) :
        if a[i] == a[j] :
            check = False
            break
    if check :
        print(a[i], end=' ')
        
# 방법 3
for i in range(len(a)):
	check = False
	for j in range(i + 1):
		if i != j and a[i] == a[j]:
			check = True
			break
	
	if check == False:
		print(a[i], end=" ")