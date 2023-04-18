'''
    [문제]
         a이차리스트에 값(1~100)을 9개 저장 후
         내림차순 정렬하시오.
    [예시]
        정렬 전 >>>
        [72, 23, 40]
        [67, 62, 88]
        [57, 54, 48]

        b = [72, 23, 40, 67, 62, 88, 57, 54, 48] 
        b :  [88, 72, 67, 62, 57, 54, 48, 40, 23]
        
        정렬 후 >>>
        [88, 72, 67]
        [62, 57, 54]
        [48, 40, 23]
'''
import random

a = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
b = []

print('정렬 전 >>>')
for i in range(len(a)) :
    for j in range(len(a[i])) :
        a[i][j] = random.randint(1,100)
        b.append(a[i][j])
    print(a[i])

print()
print(f'정렬 전 b = {b}')


for i in range(len(b)) :
    maxIndex = i
    maxNum = b[i]
    
    for j in range(i,len(b)) :
        if maxNum < b[j] :
            maxNum = b[j]
            maxIndex = j
    
    temp = b[i]
    b[i] = maxNum
    b[maxIndex] = temp

print(f'정렬 후 b = {b}')

print('정렬 후 >>>')
index = 0
for i in range(len(a)) :
    for j in range(len(a[i])) :
        a[i][j] = b[index]
        index += 1
    print(a[i])




    