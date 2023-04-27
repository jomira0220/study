'''
    [문제]
        철수는 a리스트에서 숫자 검사를 해야한다.
        각 단어를 검사해서 해당 메시지 중 하나를 출력하시오.
    [정답]
        문자만 있다
        숫자만 있다
        문자와 숫자가 섞여있다.
'''
a = ["adklajsiod", "123123", "dasd12312asd"]
msg = ["문자만 있다", "숫자만 있다", "문자와 숫자가 섞여있다."]


num = '0123456789'
for i in range(len(a)):
    check = False
    count = 0
    for j in range(len(a[i])):
        for p in range(len(num)):
            if num[p] == a[i][j]:
                check = True
                count += 1
    if count == len(a[i]) :
        print(msg[1])
    elif check == False :
        print(msg[0])
    else :
        print(msg[2])
        

