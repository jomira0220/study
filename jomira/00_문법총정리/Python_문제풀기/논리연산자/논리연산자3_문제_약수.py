'''	
	[문제] 
        아래 변수의 a값이 
        100의 자리가 30의 약수 이거나 10의 자리가 25의 약수이면,
        True 출력하시오.
	[정답]
		True
'''
a = 3240

b = a % 1000 // 100
c = a % 100 // 10
print(c)
print(30 % b == 0 or 25 % c == 0)