# 파이썬 문자열

# 큰따옴표, 작은따옴표 모두 허용한다.
txt1 = "python"
txt1 = 'python'

# 작은따옴표를 출력 => 큰따옴표 감싸기
print("'python'")
# 큰따옴표 출력 => 작은따옴표 감싸기
print('"python"')


# 곱하기 연산자[반복자]
txt3 = "python" * 3

# 더하기 연산자[연결자]
txt4 = "py" + "thon"
print(txt4)
# 타입이 맞지않으면 오류남 => txt4 = "py" + 1


# 문자열 길이 : len()
print(len(txt4))


# 형변환
# (1) 문자 -> 숫자 : int()
# (2) 숫자 -> 문자 : str()
strNum = "10"
print(int(strNum) + 1 ) #11


num = 3
print(str(num) + "학년")

# 문자열 (수정불가한 데이터, immutable)
txt5 = "hello, python"
#수정불가 -> txt5[5] = "1"

txt5.replace(",","!") 
# 원본 자체를 수정하는것이 아니기 때문에
# 원본을 수정하려면 아래와 같이 대입시켜줘야함
txt5 = txt5.replace(",","!") 
print(txt5)

