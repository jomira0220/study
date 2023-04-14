'''
   [문제]
      a리스트에 랜덤(1~4) 숫자 4개를 저장한다. 
      단, 중복없는 숫자로 저장한다.
   
   [예시]
      [1,4,2,3]
'''
import random

a = [0, 0, 0, 0]
check = [False, False, False, False]

count = 0
while True :
    index = random.randint(1,4) - 1
    if check[index] == False :
        a[count] = index + 1
        check[index] = True
        count += 1
    if count == 4 :
        break
    
    
print(a)
    