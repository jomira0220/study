'''
[문제]
    0에서 100사이의 랜덤 숫자를 시험 점수로 저장한다.
    시험점수에 해당하는 학점을 출력하시오.
    아래는 점수표이다.
    100~91 이면 A학점,
    90~81  이면 B학점,
    80이하는 "재시험"
    
    단, 만점이거나, A학점과 B학점의 일의 자리가 8점이상이면 + 기호를 추가하시오.
    [예] 
        100 => A+
        88 ==> B+
        82 ==> B
        23 ==> 재시험
'''
'''
    랜덤을 테스트할 때는 원하는 값이 나올 때까지 무한반복을 하게된다.
    아래와 같이 일정 숫자가 나오도록 폭을 조정하면 테스트하기 쉽다. 
'''

# 100(A+) / 98(A+) / 91(A) / 88(B+) / 82(B) / 51(재시험)

import random
score = random.randint(0,100)
score = 91
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