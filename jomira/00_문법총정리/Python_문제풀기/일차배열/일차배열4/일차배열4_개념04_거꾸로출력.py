'''
    [문제]	
        a의 값들을 거꾸로 출력하시오.
    [정답]
        60 54 12 44 21 
'''
a = [21, 44, 12, 54, 60]

a.reverse()
print(a)

'''
#[방법2]
a = a[::-1]
print(a)


#[방법3]
a = list(map(str,a))
a.reverse()
a = list(map(int,a))
print(a)
'''