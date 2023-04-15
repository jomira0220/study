'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
  
	[예시]
		**
		****
		******
		********
'''


for i in range(4) :
    for j in range((i+1)*2) :
        print('*',end=' ')
    print()