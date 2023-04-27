'''
    [문제]
        member는 회원목록이다.
        item은 쇼핑몰 판매상품이다.
        price는 아이템 가격이다.
        
        order는 오늘 주문 목록이다. 
        cancel은 주문취소 목록이다.
        오늘의 매출을 출력하시오.
    [정답]
        7700
'''

member = "qwer1234,pythongood,testid"
item   = "사과,1100/바나나,2000/딸기,4300"
order  = "qwer1234,사과,3/phthongood,바나나,2/qwer1234,딸기,5/testid,사과,4"
cancel = "qwer1234,딸기,5/phthongood,바나나,2"


member = member.split(',')

def splitStr(str,a,b):
    arr = str.split(a)
    for i in range(len(arr)):
        arr[i] = arr[i].split(b)
    return arr

item = splitStr(item,'/',',')
order = splitStr(order,'/',',')
cancel = splitStr(cancel,'/',',')
    
print('member = {}'.format(member))
print('item = {}'.format(item))
print('order = {}'.format(order))
print('cancel = {}'.format(cancel))

total = 0
for i in range(len(order)):
    check = True
    orderCount = int(order[i][2])
    
    #취소한 주문이 있는지 확인하여 주문취소개수만큼 주문수량 차감
    for j in range(len(cancel)):
        if order[i][0] == cancel[j][0] and order[i][1] == cancel[j][1] :
            orderCount -= int(cancel[j][2])
            
    # 주문수량에 맞춰서 토탈금액 계산
    for j in range(len(item)):
        if order[i][1] == item[j][0] :
            total += int(item[j][1]) * orderCount

print(total)