'''
	[문제]
		복권 1개당 7칸으로, 총 5개의 복권을 제작하려 한다.
		복권 1줄은 1 또는 7의 랜덤 숫자로 구성되어 있다.
		7이 연속으로 3개 이상이면 "당첨"이고, 그 미만은 "꽝"이다.
		5개 중에 딱 1개만 당첨 복권이고 나머지 4개는 꽝인 복권을
		랜덤으로 생성해서 출력하시오.
		
		예)
			1177117 (꽝)
			1117771 (당첨)
			7171117 (꽝)
			7711771 (꽝)
			7171717 (꽝)
'''
import random

'''
for i in range(5):
    num7Count = 0
    num1Count = 0
    temp = []
    for j in range(7):
        num = random.randint(0,1)
        if num == 0 :
            num = 7
            num7Count += 1
            if num7Count > 3 :
                num = 1
        if num == 1 :
            num1Count += 1
            if num1Count > 4 :
                num = 7
        temp.append(num)
    print(temp,end=' ')
    
    count = 0
    for j in temp:
        if j == 7 :
            count += 1
            if count == 3 :
                print('당첨')
                break
        else :
            count = 0
        
    if count != 3 : print('꽝')
'''    
lottoList = []
checkList = []
i = 0
while True :
    
    num7Count = 0
    num1Count = 0
    lottoList.append([])

    for j in range(7):
        num = random.randint(0,1)
        if num == 0 :
            num = 7
            num7Count += 1
            if num7Count > 3 :
                num = 1
        if num == 1 :
            num1Count += 1
            if num1Count > 4 :
                num = 7
        lottoList[i].append(num)

    count = 0
    check = False
    for j in lottoList[i]:
        if j == 7 :
            count += 1
            if count == 3 :
                checkList.append('당첨')
        else :
            count = 0
            check = True
    
    if check : checkList.append('꽝')
    
    당첨 = 0
    for j in checkList:
        if j == '당첨':
            당첨 += 1
    
    if 당첨 == 1 and i == 4:
        for j in range(5) :
            print(lottoList[j],end=' ')
            print(checkList[j]) 
        break
    elif 당첨 != 1 or i == 4 :
        checkList = []
        lottoList = []
        i = 0
        continue
    
    i += 1



    
    
    

        
    



    
    