'''
	[문제]
		철수는 농구공을 12번 던져 7번 성공했다.
		영희는 농구공을 17번 던져 9번 성공했다.
		영희의 성공확률이 철수의 성공확률보다 더 높은지
    그 결과를 True 또는 False로 구하시오.
		위 내용을 비교연산자로 표현하시오.
  [정답]
      False
'''
import math
철수 = math.trunc(100 / 12 * 7)
영희 = math.trunc(100 / 17 * 9)
result = 철수 < 영희
print(철수)
print(영희)
print(result)