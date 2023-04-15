'''
	[문제]
		이번 달 1일이 수요일이라고 할 때, 
		랜덤으로 1~31을 저장하고 해당 요일을 출력하시오.

		[예]
		3일 ==> 금요일
'''

import random 
day = random.randint(1,31)
print(day)
result = '월'
if day % 7 == 1 :
    result = '수'
elif day % 7 == 2 :
    result = '목'
elif day % 7 == 3 :
    result = '금'
elif day % 7 == 4 :
    result = '토'
elif day % 7 == 5 :
    result = '일'
elif day % 7 == 6 :
    result = '월'
elif day % 7 == 0 :
    result = '화'
    
print(result+'요일')