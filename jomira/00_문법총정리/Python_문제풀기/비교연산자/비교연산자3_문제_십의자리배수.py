'''	
	[문제] 
     아래 변수의 a의 값이 
     10의 자리가 3의 배수이면, True를 출력하시오.
'''
a = 3340

print((a % 100 // 10) % 3 == 0)