'''
# 반복문 while
	* 5회 반복 요청
	1 ~ 5  +1	1, 2, 3, 4, 5
	1 ~ 10 +2 	1, 3, 5, 7, 9
	5 ~ 1  -1	5, 4, 3, 2, 1

	[1] 반복의 조건 3가지
		1) 초기식
		2) 조건식
		3) 증감식

	[2] 구조
		(1) 초기식
			i = 1
		(2) 조건식
			1) while i <= 5:
			2) 조건식이 참일 동안 실행할 문장
			3) 들여쓰기한다.
		(3) 증감식
			1) i = i + 1
			2) 들여쓰기한다.
'''

# [문제] 1부터 5까지 출력하시오.

i = 1					# 초기식

while i <= 5:			# 조건식
    print(i) # 1 2 3 4 5
    i = i + 1			# 증감식
    

for i in range(1,10,2):
    print(i, end= " ") # 1 3 5 7 9 5 번 실행됨
print()


# break
i = 1
while True:
    print(i, end=" ") # 1 2 3
    if i == 3:
        break
    i += 1
print()

# continue
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i, end=" ") # 1 2 4 5
    i += 1


#이차반복문
for i in range(2,10):
	print(i, "단>>>")
	for j in range(1,10):
            print(i, "X", j, "=", i*j)
        

for i in range(-5, 6):
    print(i, end=" ")
print()


#이차반복문

list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(id(list[0]))
print(id(list[1]))
print(id(list[2]))

print(list[0])
print(list[1])
print(list[2])

list[0] = list[1]
list[1][0] = 100

print(id(list[0]))
print(id(list[1]))
print(id(list[2]))

print(list[0])
print(list[1])
print(list[2])
