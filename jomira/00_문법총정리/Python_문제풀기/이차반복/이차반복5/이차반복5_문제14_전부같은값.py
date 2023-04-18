'''
	[문제]
		a리스트와 b리스트의 값들이 각각 값과 개수가 똑같은지 확인한다.
		똑같으면 "같음", 아니면 "다름"을 출력하시오.
		위치는 상관없이 각각의 숫자의 개수가 일치하면 "같음"이다. 
	[정답]
'''
a = [10, 20, 30, 10, 20, 30]
b = [30, 20, 10, 20, 30, 10]

'''
a = sorted(a)
b = sorted(b)

print(a)
print(b)

count = 0
if len(a) == len(b) :
    for i in range(len(a)) :
        if a[i] == b[i] : 
            count += 1
    if count == len(a) :
        print('같다')
    else :
        print('다르다')
'''

check = True
size = len(a)
for i in range(size) :
    countA = 0
    countB = 0
    for j in range(size) :
        if a[i] == b[j] :
            countA += 1
        if b[i] == a[j] :
            countB += 1
    
    if countA != countB :
        check = False
    
if check :
    print('같음')
else :
    print('다름')