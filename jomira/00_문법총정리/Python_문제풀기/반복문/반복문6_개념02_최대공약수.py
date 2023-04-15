'''
[문제]
	90과 45의 최대공약수를 출력하시오.
[출력]
	45
'''

i = 1
result = 0
while i <= 45 :
    if 90 % i == 0 and 45 % i == 0 :
        result = i
    i += 1
    
print(result)