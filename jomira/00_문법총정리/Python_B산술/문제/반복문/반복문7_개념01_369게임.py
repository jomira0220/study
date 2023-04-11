'''
[문제]
    1. 1~50까지 반복한다.
    2. 그 안에서 해당 숫자의 369게임의 결과를 출력한다.
    3. 각각의 숫자에 3이나 6이나 9가 두 개면 "짝짝"
    4. 각각의 숫자에 3이나 6이나 9가 한 개면 "짝"
    5. 3이나 6이나 9가 없으면 그냥 숫자를 출력하시오.
    
[결과] 
    1 2 짝 4 5 짝 7 8 짝 10 11 12 짝 ...
'''
'''
    36 // 10 = 3
    36 % 10  = 6
'''

i = 1

while i <= 50 :
    
    count = 0
    일자리 = i % 10
    십자리 = i // 10
    
    if 일자리 == 3 or 일자리 == 6 or 일자리 == 9 :
        count += 1
        
    if 십자리 == 3 or 십자리 == 6 or 십자리 == 9 :
        count += 1
        
    if count == 2 :
        print('짝짝')
    elif count == 1 :
        print('짝')
    else :
        print(i)
        
    i += 1