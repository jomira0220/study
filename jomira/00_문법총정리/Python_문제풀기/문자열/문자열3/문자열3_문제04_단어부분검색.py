'''
    [문제]
        a리스트는 단어들이 모여있는 리스트이다.
        search는 검색하고 싶은 단어이다.
        a리스트에서 해당 단어를 검색해서 출력하시오.
        단, 부분 검색도 되어야한다.
        
    [예시] 
        school, teacher, child
'''


a =["school", "teacher", "child","father", "love"]

search = "ch"

for i in range(len(a)):
    check = False
    for j in range(len(a[i])-1):
        count = 0
        for p in range(len(search)):
            if a[i][j+p] == search[p]:
                count += 1
                if count == 2 :
                    check = True
            else:
                count = 0
    if check : print(a[i],end=', ')