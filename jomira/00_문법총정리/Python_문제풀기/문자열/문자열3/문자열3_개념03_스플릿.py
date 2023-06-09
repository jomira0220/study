'''
    [문자열 구분자]
        문자열로 데이터를 저장할 때는 보통 구분자를 사용한다.
        이런 문자열을 쉽게 리스트로 변환해주는 split() 함수가 있다.
'''

# [일차원 구분자]
text = "80,3,23"
a = text.split(",")
print(a)


# [이차원 구분자]
text = "1001,김철수/1002,이민수/1003,신영희"
temp = text.split("/") 
print(temp) # ['1001,김철수', '1002,이민수', '1003,신영희'] 먼저 / 로 잘라낸다.
a = []
for i in range(len(temp)):
    temp2 = temp[i].split(",") # 각 데이터 '1001,김철수' 를 다시 ,를 기준으로 잘라낸다.
    a.append(temp2)
    
print(a)