'''
    [문제]
        0에서 100 사이의 랜덤 숫자를 시험 점수로 저장한다.
        시험점수에 해당하는 학점을 출력하시오.
        아래는 점수표이다.
        100~91 이면 A학점,
        90~81  이면 B학점,
        80 이하는 "재시험"
        
        단, 만점이거나, A 학점과 B 학점의 일의 자리가 8점 이상이면 + 기호를 추가하시오.
        [예] 
            100 => A+
            88 ==> B+
            82 ==> B
            23 ==> 재시험
'''
import random 

score = random.randint(0,100)
score = 87
print(score)

일 = score % 10

result = ''
if score >= 91 :
    result = 'A'
    if 일 >= 8 or score == 100 :
        result += '+'
elif score >= 81 :
    result = 'B'
    if 일 >= 8 :
        result += '+'
else :
    result = '재시험'
    
print(result)
