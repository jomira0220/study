'''
    [문제]
        [조건1] 리스트에 랜덤 숫자(1~100) 다섯 개를 추가한다.
        [조건2] 위 값 중에 5의 배수들만 출력하시오.
    [예시]
        arr = [70, 87, 61, 4, 81]
        70
'''
import random
arr = []

for i in range(5) :
    arr.append(random.randint(1,100))
    if arr[i] % 5 == 0 : print(arr[i],end=' ')
    
print()
print(arr)