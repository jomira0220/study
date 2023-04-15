'''
	[문제]	  
		철수는 최근 무인도를 구입하고, 그 나라의 왕이 되었다.
		평소 월요병이 있던 철수는 일주일에서 월요일을 삭제하였다.
		만약 이번 달 1일이 일요일일 때, 랜덤으로 1~31을 저장하고,
		해당 날짜의 요일을 출력하시오.

		[예]
			1 : 일요일
			2 : 화요일
			3 : 수요일
			4 : 목요일
			5 : 금요일
			6 : 토요일
			7 : 일요일
			8 : 화요일 
			...
'''

import random
day  = random.randint(1,31)
unit = day % 6
result = ''
if unit == 1 :
    result = '일'
elif unit == 2 :
    result = '화'
elif unit == 3 :
    result = '수'
elif unit == 4 :
    result = '목'
elif unit == 5 :
    result = '금'
elif unit == 0 :
    result = '토'
    
print(day,':',result+'요일')