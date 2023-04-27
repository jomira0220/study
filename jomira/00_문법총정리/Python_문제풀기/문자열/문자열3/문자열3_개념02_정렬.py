'''
    [문자열 정렬]
        문자도 숫자와 같이 해당 문자에 해당하는 숫자로 되어있다.
        예를 들어 a가 1이면 b는 2이다. 
        크다 작다로 비교할 수 있다.
'''
a = ["aa", "ee", "cc", "dd", "bb"]
'''
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] < a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
'''           
a = sorted(a)            
print(a)