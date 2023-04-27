'''
    [문제]
        아래 데이터는 학생점수데이터이다. 
        번호, 이름, 점수 이렇게 한 세트이다.
        일등을 삭제하고 다시 문자열로 만드시오.
    [정답]
        1001,김철수,17/1003,신민아,49
'''
text = "1001,김철수,17/1002,이민수,80/1003,신민아,49"
temp = text.split("/")

a = []
for i in range(len(temp)):
    a.append(temp[i].split(','))
print(a)

maxScore = 0
check = 0
for i in range(len(a)):
    if int(a[i][2]) > maxScore :
        maxScore = int(a[i][2])
        check = i

del a[check]
print(','.join(a[0]),end='/')
print(','.join(a[1]))

