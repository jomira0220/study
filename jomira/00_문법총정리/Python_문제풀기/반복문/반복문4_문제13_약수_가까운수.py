'''
	[문제] 
		200의 약수 중에서 짝수 중 
		80에 가장 가까운 수를 구하시오.
		만약 약수 중에 80이 있을 경우, 80이 정답이다.
	[정답]
		100
'''
i = 1
num = 200
front = 0
back = 0
count = 0
while i <= num :
    if num % i == 0 :
        if i > 80 or i == 80:
            count += 1 
            if count == 1 :
                back = i
                break
        elif i < 80 :
            front = i
            
    i += 1
    
if num - front < num - back :
    print(front)
else :
    print(back)
