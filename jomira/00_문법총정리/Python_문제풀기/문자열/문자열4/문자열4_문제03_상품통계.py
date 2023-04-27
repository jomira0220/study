'''
    [문제]
        memberList는 회원목록데이터이다.
        number 는 회원 번호이다. 
        id 는 회원아이디이다.

        itemList은 쇼핑몰 판매상품데이터이다.
        itemName 는 상품이름이다.
        price는 아이템 가격이다.
        
        orderList는 오늘 주문 목록이다. 
        orderid 는 주문한 회원 id 이다.
        itemname 는 주문한 상품이름이다. 
        count 는 주문한 상품개수이다. 
        
        각아이템별로 구입한 회원이름과 개수를 구하시오.
        단, 주문목록에 없는 아이템은 구하지않는다. 
    [정답]
        {'itemName': '고래밥', 'name': '이만수', 'count': 1}
        {'itemName': '고래밥', 'name': '김철민', 'count': 1}
        {'itemName': '새우깡', 'name': '이만수', 'count': 1}
        {'itemName': '새우깡', 'name': '김철민', 'count': 1}
        {'itemName': '새우깡', 'name': '이영희', 'count': 3}
        {'itemName': '감자깡', 'name': '이영희', 'count': 1}
        {'itemName': '감자깡', 'name': '이만수', 'count': 1}
        {'itemName': '칸쵸', 'name': '이영희', 'count': 1}
        {'itemName': '빼빼로', 'name': '박민재', 'count': 1}
        {'itemName': '빼빼로', 'name': '이만수', 'count': 1}
        {'itemName': '고구마깡', 'name': '김철민', 'count': 2}
'''
memberList = [
    {"memberNumber" : 3001 , "name" : "이만수"},
    {"memberNumber" : 3002 , "name" : "김철민"},
    {"memberNumber" : 3003 , "name" : "이영희"},
    {"memberNumber" : 3004 , "name" : "조성아"},
    {"memberNumber" : 3005 , "name" : "박민재"},
]
itemList = [
    {"itemNumber" : 100001 , "itemName" : "고래밥"},
    {"itemNumber" : 100002 , "itemName" : "새우깡"},
    {"itemNumber" : 100003 , "itemName" : "감자깡"},
    {"itemNumber" : 100004 , "itemName" : "칸쵸"},
    {"itemNumber" : 100005 , "itemName" : "오징어땅콩"},
    {"itemNumber" : 100006 , "itemName" : "빼빼로"},
    {"itemNumber" : 100007 , "itemName" : "고구마깡"},
]
orderList = [
    {"memberNumber" : 3001 , "itemNumber" : 100001},
    {"memberNumber" : 3001 , "itemNumber" : 100002},
    {"memberNumber" : 3003 , "itemNumber" : 100004},
    {"memberNumber" : 3002 , "itemNumber" : 100007},
    {"memberNumber" : 3003 , "itemNumber" : 100003},
    {"memberNumber" : 3005 , "itemNumber" : 100006},
    {"memberNumber" : 3002 , "itemNumber" : 100002},
    {"memberNumber" : 3001 , "itemNumber" : 100007},
    {"memberNumber" : 3003 , "itemNumber" : 100002},
    {"memberNumber" : 3002 , "itemNumber" : 100001},
    {"memberNumber" : 3001 , "itemNumber" : 100003},
    {"memberNumber" : 3003 , "itemNumber" : 100002},
    {"memberNumber" : 3002 , "itemNumber" : 100007},
    {"memberNumber" : 3001 , "itemNumber" : 100006},
    {"memberNumber" : 3003 , "itemNumber" : 100002},
]

totalList = []


for i in range(len(itemList)):
    name = ""
    item = itemList[i]
    for j in range(len(orderList)):
        order = orderList[j]
        for k in range(len(memberList)):
            member = memberList[k]
            if member["memberNumber"] == order["memberNumber"]:
                name = member["name"]
                break 
        if item["itemNumber"] == order["itemNumber"]:           
            check = False
            for k in range(len(totalList)):
                total = totalList[k]
                if total["itemName"] == item["itemName"] and name == total["name"]:
                    check = True
                    total["count"] += 1
                    break                
            if check == False:
                temp = {"itemName" : item["itemName"] , "name" :  name , "count" : 1}
                totalList.append(temp)

for i in range(len(totalList)):
    print(totalList[i])

