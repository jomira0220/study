'''
	[문제]
		철수는 13살 철수의 아버지는 45살이다. 
		몇 년 후 철수의 아버지는 철수 나이의 3배가 될지 구하시오.
	[정답]
		3
'''
철수 = 13
아버지 = 45
i = 1
run = 1
while run == 1 :
    if (철수 + i) * 3 == 아버지 + i :
        print(i)
        break
    i += 1