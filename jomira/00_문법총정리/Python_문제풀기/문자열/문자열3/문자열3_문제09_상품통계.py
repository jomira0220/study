'''
    [문제]
        member는 회원목록이다.
        item은 쇼핑몰 판매상품이다.
        order는 오늘 주문목록이다.
        회원별 아이템 주문개수를 출력하시오.
    [정답]
        이만수: 고래밥 3
        김철민: 고래밥 1 칸쵸 1
        이영희: 새우깡 2 칸쵸 1
'''

member  = "3001/이만수,3002/김철민,3003/이영희"
item    = "1001/고래밥,1002/새우깡,1003/칸쵸"
order   = "3001,1001/3001,1001/3003,1002/3002,1003/3001,1001/3003,1002/3003,1003/3002,1001"


def splitStr(str,a,b) :
    arr = str.split(a)
    for i in range(len(arr)):
        arr[i] = arr[i].split(b)
    return arr

member = splitStr(member,',','/')
item = splitStr(item,',','/')
order = splitStr(order,'/',',')

print('member = {}'.format(member))
print('item = {}'.format(item))
print('order = {}'.format(order))


for i in range(len(member)):
    itemCount = [['고래밥',0],['새우깡',0],['칸쵸',0]]
    for j in range(len(order)):
        if member[i][0] == order[j][0] :
            for p in range(len(item)):
                if item[p][0] == order[j][1]:
                    itemCount[p][1] += 1
    print(member[i][1],end=': ')
    print(itemCount)