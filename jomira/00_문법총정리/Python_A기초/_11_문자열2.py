# 문자열의 인덱싱과 슬라이싱
text = "hello, python"

# 인덱싱(indexing)
print(text[0])

# 슬라이싱(slicing)
# 0부터 5미만까지 추출
print(text[0:5])
print(text[:5]) # 첫자리 0은 기본값으로 생갹해도 무방


#
print(len(text))
# 7부터 13미만까지 추출
print(text[7:len(text)])
print(text[7:]) # 뒷자리는 자동으로 마지막 숫자 들어가므로 생략해도 무방
