'''
	[문제]	  	
		마트에서 오이를 3개씩 묶어서 1500원에 판매한다.
		오이가 14개 필요하다면,
		필요한 금액을 출력하시오.
		단, 오이는 묶음으로만 판매한다.
	[정답]
		7500
'''
import math
구매개수 = math.ceil(14 / 3)
지불가격 = 구매개수 * 1500

print(지불가격)