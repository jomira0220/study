'''
    [문자열 비교]
        info리스트는 학생 정보이다.
        search리스트의 내용이 info에 있으면 o 없으면 x를 출력하시오. 
    [정답]
        이민수o
        김철수o
        김상진x
'''
info = ["김철수" , "이민수" , "유영희", "이민정", "조아라"]
search = ["이민수", "김철수", "김상진"]


for i in search:
    check = False
    for j in info:
        if i == j :
            check = True
    if check :
        print(i,'O')
    else :
        print(i,'X')