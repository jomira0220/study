'''
	[문제]
		철수는 볼펜을 10~30개를 구입해야 한다. 
		
		볼펜 하나의 가격은 1200원이다. 	
		볼펜은 20개 이상 구매 시 볼펜 한 개에 100원을 할인해주고 있다. 
			
		볼펜 수를 랜덤으로 저장하고,
		철수가 지급해야 하는 금액을 출력하시오.
		[예]
			볼펜 수 = 22
			지급 금액 = 22 * 1100 = 24200
'''

import random

볼펜수 = random.randint(10,30)
볼펜한개가격 = 1200
지불금액 = 볼펜수 * 볼펜한개가격

if 볼펜수 >= 20 :
    지불금액 = 지불금액 - 볼펜수 * 100
    
    
print('볼펜수 =',볼펜수)
print('지불금액 =',지불금액)