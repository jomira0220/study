'''
  [문제]
    가게 A에서 한 개에 1000원인 음료수가 가게 B에서는 한 개에 500원이라고 한다.
    가게 B에 다녀오려면 왕복 교통비가 1600원이 들 때, 음료수를 몇 개 이상 살 경우
    가게 B에서 사는 것이 더 유리한지 구하시오.
  
		위 식을 표현하고, 풀이 과정을 주석으로 작성하시오.
'''

'''
1000 * a >= 500 * a + 1600
1000a >= 500a + 1600
500a >= 1600
a >= 1600 / 500
'''

print(1600/500)