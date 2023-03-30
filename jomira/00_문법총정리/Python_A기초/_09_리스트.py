# 리스트 함수
list = []

# 맨뒤에 추가 : append()
# list[0] = 10 //배열이 비어잇는 경우 - IndexError: list assignment index out of range
list.append(10)
list.append(20)
list.append(30)
print(list)

# 수정
list[1] = 100
print(list)

# 삭제
#   1) remove(값) 
#   2) del 값
list = [10,20,30,40,50]
list.remove(20)
print(list) # [10, 30, 40, 50]

del list[1]
print(list) # [10, 40, 50]

# 인덱스 검색 - index(값)
list = [10,20,30,40,50]

# delIndex = list.index(20)
# del list[delIndex]
del list[list.index(20)]
print(list) # [10, 30, 40, 50]

