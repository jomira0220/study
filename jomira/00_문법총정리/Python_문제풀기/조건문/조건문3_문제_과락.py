'''
	[문제]
		[1] 0에서 100 사이의 랜덤 점수 2개를 저장해 평균을 구한다.
		[2] 평균이 60점 이상이면 합격, 60점 미만이면 불합격이다.
		[3] 단, 평균이 60 이상이라도, 한 과목이라도 50 미만이면 불합격을 출력하시오.
'''
import random
score1 = random.randint(0,100)
score2 = random.randint(0,100)
avg = (score1 + score2) / 2
result = '불합격'
if avg >= 60 and score1 >= 50 and score2 >= 50 :
    result = '합격'
    
print(result)