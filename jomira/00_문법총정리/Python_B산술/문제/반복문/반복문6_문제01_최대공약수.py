'''
	[문제] 
		45와 60, 75의 최대공약수를 구하시오.
	[정답]
		15
'''

i = 1
result = 0
while i <= 75 :
    if 45 % i == 0 and 60 % i == 0 and 75 % i == 0 :
        result = i
    i += 1
    
print(result)