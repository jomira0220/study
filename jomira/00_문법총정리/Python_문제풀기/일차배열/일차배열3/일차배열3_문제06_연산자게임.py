'''
	[테스트]
		a 와 b의 각 자리의 숫자끼리 더하기 또는 빼기 또는 곱하기를 해서 total에 저장하려 한다.
		더하기, 빼기, 또는 곱하기는 op의 값으로 정한다. 
		op 가 0 이면 더하기 
		op 가 1 이면 빼기
		op 가 2 이면 곱하기이다. 
  
	[정답]
		(1) a = 3 , b = 5 , op = 0 은 더하기이다 : total = [8]
		(2) a = 4 , b = 3 , op = 1 은 빼기이다   : total = [8 , 1]
		(3) a = 2 , b = 1 , op = 0 은 더하기이다 : total = [8 , 1 , 3]
		(4) a = 8 , b = 7 , op = 2 는 곱하기이다 : total = [8 , 1 , 3 , 56]
		(5) a = 6 , b = 3 , op = 1 은 빼기이다   : total = [8 , 1 , 3 , 56 , 3]

		total = [8, 1, 3, 56, 3]
'''

a = [3, 4, 2, 8, 6]
b = [5, 3, 1, 7, 3]

op = [0, 1, 0, 2, 1]

total = []
opment = ''
for i in range(len(op)) :
    if op[i] == 0 :
        total.append(a[i] + b[i])
        opment = '더하기'
    elif op[i] == 1 :
        total.append(a[i] - b[i])
        opment = '빼기'
    else :
        total.append(a[i] * b[i])
        opment = '곱하기'
        
    print(f'a = {a[i]}, b = {b[i]}, op = {opment}, total = {total}')

print(f'total = {total}')