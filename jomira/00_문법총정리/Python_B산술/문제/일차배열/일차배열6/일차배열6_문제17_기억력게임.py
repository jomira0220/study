'''
     [문제]
      1. 같은 숫자가 적혀있는 카드 2장씩 5세트가 있다. (총10장)
      2. front는 카드를 엎어놓은 상태를 뜻한다. 
      3. 먼저 front를 셔플한다. 
      4. front에 있는 카드 2개를 랜덤으로 선택한다. (마우스가 없으므로 인덱스로 선택)
      5. 선택한 카드 2장의 내용이 같으면 back에 복사해서 맞춘 걸 표시한다. 
         back에 모든 글자가 채워지면 게임은 종료된다.
         
      6. 같은 인덱스 선택할 수 없다. 
      7. 이미 선택한 자리를 또 선택할 수 없다. 
'''
import random

front = [10,10,20,20,30,30,40,40,50,50]
back = [0,0,0,0,0,0,0,0,0,0]

# 파이썬 셔플 함수
random.shuffle(front)
print(front)


count = 0
while True :
    print()
    # 카드 두개 랜덤 선택
    card_1 = random.randint(0,len(front)-1)
    card_2 = random.randint(0,len(front)-1)
    while True :
        if card_1 != card_2 :
            break
        else : card_2 = random.randint(0,len(front)-1) 

    print(f'front[{card_1}] = {front[card_1]},', end=' ')
    print(f'front[{card_2}] = {front[card_2]}')

    if front[card_1] == front[card_2] :
    
        if back[card_1] == 0 and back[card_2] == 0 :
            back[card_1] = front[card_1]
            back[card_2] = front[card_2]
            count += 1
            print('값이 같다!')
        else :
            print('이미 선택한 자리입니다!')
    else :
        print('값이 다르다!')
        
    print(f'count = {count}')

    # back에 모든 글자가 채워지면 종료
    # 두개씩 채워지므로 다 채워지면 count는 5개임
    if count == len(back) // 2 : break
    
    


print(back)