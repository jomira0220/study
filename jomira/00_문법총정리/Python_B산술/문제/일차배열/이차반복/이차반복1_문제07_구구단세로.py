'''
	[문제]
		아래와 같이 2단부터 9단까지 구구단을 출력해보시오. 
		단, 이차 반복문을 사용한다. 
	
 	[예시]
		2 X 1 = 2
		2 X 2 = 4
		2 X 3 = 6
		2 X 4 = 8
		2 X 5 = 10
		2 X 6 = 12
		2 X 7 = 14
		2 X 8 = 16
		2 X 9 = 18
  
		3 X 1 = 3
		3 X 2 = 6
  		3 X 3 = 9
		3 X 4 = 12
		...
		...

		9 X 8 = 72
		9 X 9 = 81
'''


for front in range(2,10) :
    for back in range(1,10) :
        print(f'{front} X {back} = {front*back}')
    print()
    