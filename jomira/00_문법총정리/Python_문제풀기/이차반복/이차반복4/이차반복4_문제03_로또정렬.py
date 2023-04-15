'''
	[문제] 
		1~45사이의 랜덤값 6개를 lotto에 저장하려 한다.
		단, 중복되는 숫자는 없어야 하며,
		내림차순 정렬 후 출력하시오.
	[예시]
        [40, 38, 27, 26, 18, 5]
'''


import random 

lotto = []


while True :
    num = random.randint(1,45)
    check = True
    for i in lotto :
        if num == i :
            check = False
            break
    if check :
        lotto.append(num)
    if len(lotto) == 6 :
        break

lotto = sorted(lotto,reverse=True)
print(lotto)