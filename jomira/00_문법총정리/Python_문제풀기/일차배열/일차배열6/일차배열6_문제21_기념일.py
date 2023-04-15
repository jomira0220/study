'''
	[문제]	
		철수와 영희는 3월 3일에 만났다. 		
		철수는 영희와 100일 기념일에 축하 파티를 하려 한다.
		만난 지 100일 뒤는 몇 월 며칠인지 구하시오.
		단, 윤년은 계산하지 않으며,
		시작일은 포함시키지 않는다.
	[정답]
		6월 11일
'''

monthList =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = 3
day = 3

total = 0
start = monthList[month-1] - 3 # 3월 4일부터 시작카운트
for i in range(100) :
    start -= 1
    if start == 0 :
        month += 1
        start = monthList[month]

print(f'{month}월 {monthList[month]-start}일')