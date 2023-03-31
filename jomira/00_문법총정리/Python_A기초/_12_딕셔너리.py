# 딕셔너리

# 딕셔너리 = 자바스크립트의 JSON 객체,배열

# 빈 리스트 생성 방법
a = []
a = list()

# 빈 딕셔너리 생성 방법
b = {}
b = dict()

dic = {
    # key : value
    "이름": "홍길동",
    "나이": 20,
    "성별": "남",
}

print(dic["이름"])

print()

# key만 출력 함수 : keys(), 리스트로 리턴됨
keysTest = dic.keys()
print(keysTest)

for i in keysTest:
    print(dic[i])


print()

# value만 출력 함수 : values(), 리스트로 리턴됨
valuesTest = dic.values()
print(valuesTest)



# 딕셔너리 추가
dic["성적"] = 80
print(dic)

# 딕셔너리 삭제
del dic["나이"]
print(dic)


# get() : key값의 존재유무 확인, 예외처리를 위한 수단
val = dic.get("국어")
print(val) # 값이 없으면 None 출력

if val == None:
    print("해당 값은 존재하지 않습니다.")
else:
    print(val)
    
    
# in 키워드
if "성적" in dic:
    print(dic["성적"])
else:
    print("해당 값은 존재하지 않습니다.")
