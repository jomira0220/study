'''
    [문제]
        itemList은 쇼핑몰 판매상품데이터이다.
        itemName 는 상품이름이다.
        price는 아이템 가격이다.
        
        orderList는 오늘 주문 목록이다. 
        ordernumber 는 주문번호이다. 
        orderid 는 주문한 회원 id 이다.
        itemName 는 주문한 상품이름이다. 
        count 는 주문한 상품개수이다. 

        cancleList 는 주문취소 목록이다. 
        canclenumber 는 주문을 취소한 번호이다. 

        취소한 상품이름을 출력하시오.단, 중복되면 한번만 출력하시오.    
    [정답]   
        ['바나나', '딸기']
'''

orderList = [
    {"orderNumber" : 100001 , "orderId" : "qwer1234" , "itemName" : "사과" , "count" : 3},
    {"orderNumber" : 100002 , "orderId" : "pythongood" , "itemName" : "딸기" , "count" : 6},
    {"orderNumber" : 100003 , "orderId" : "testid" , "itemName" : "바나나" , "count" : 4},
    {"orderNumber" : 100004 , "orderId" : "pythongood" , "itemName" : "사과" , "count" : 2},
    {"orderNumber" : 100005 , "orderId" : "testid" , "itemName" : "바나나" , "count" : 7},
    {"orderNumber" : 100006 , "orderId" : "qwer1234" , "itemName" : "사과" , "count" : 2}, 
    {"orderNumber" : 100007 , "orderId" : "testid" , "itemName" : "사과" , "count" : 3}, 
]
cancelList = [
    {"cancelNumber" : 100003 },
    {"cancelNumber" : 100002 },
    {"cancelNumber" : 100005 },
]

result = []
for i in range(len(cancelList)):
    name = ''
    for j in range(len(orderList)):
        if orderList[j]["orderNumber"] == cancelList[i]["cancelNumber"] :
            check = True
            name = orderList[j]["itemName"]
    if check :
        result.append(name)
result = list(set(result)) 
print(result)       


'''
totalList = []
for i in range(len(cancleList)):
    cancle = cancleList[i]
    for j in range(len(orderList)):
        order = orderList[j]
        if cancle["canclenumber"] == order["ordernumber"]:
            check = False
            for k in range(len(totalList)):
                if totalList[k] == order["itemname"]:
                    check = True
                    break
            if check == False:              
                totalList.append( order["itemname"])
print(totalList)
'''
