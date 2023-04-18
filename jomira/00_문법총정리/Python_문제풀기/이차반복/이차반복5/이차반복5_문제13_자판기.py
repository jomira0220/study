'''
    [문제]
        철수는 자판기에 물건을 채우려고 한다. 
        vending 리스트는 현재 자판기에 남아있는 물건 개수이다.
        box리스트는 자판기에 추가할 물건 개수이며, 5개씩 4줄 총 20개 여분이 있다.
        box의 앞에서부터 순차적으로 자판기에 물건을 채워 넣는다.
        자판기는 한 줄당 최대 10개까지 채울 수 있다.
        자판기가 전부 채워지거나 box가 전부 비워지면 종료되는 프로그램을 작성하시오.
    [예시]
        vending = [7, 5, 3, 5, 3]
        box     = [5, 5, 5, 5]

        vending = [10, 5, 3, 5, 3]
        box     = [2, 5, 5, 5]    

        vending = [10, 7, 3, 5, 3]
        box     = [0, 5, 5, 5]    

        vending = [10, 10, 3, 5, 3]
        box     = [0, 2, 5, 5]

        vending = [10, 10, 5, 5, 3]
        box     = [0, 0, 5, 5]

        vending = [10, 10, 10, 5, 3]
        box     = [0, 0, 0, 5]

        vending = [10, 10, 10, 10, 3]
        box     = [0, 0, 0, 0]
    [정답] 
        vending = [10, 10, 10, 10, 3]
        box     = [0, 0, 0, 0]
'''

vending = [7, 5, 3, 5, 3]
box = [5, 5, 5, 5]

vIndex = 0
bIndex = 0
while True:
    if vending[vIndex] < 10: 
        count = 10 - vending[vIndex]
        
        if count <= box[bIndex]:
            vending[vIndex] += count
            box[bIndex] -= count
        else:
            vending[vIndex] += box[bIndex]
            box[bIndex] = 0
    
    if box[bIndex] == 0:
        bIndex += 1
    
    if vending[vIndex] == 10:
        vIndex += 1

    print("vending =", vending)
    print("box     =", box)
    print()

    if bIndex == len(box) or vIndex == len(vending):
        break