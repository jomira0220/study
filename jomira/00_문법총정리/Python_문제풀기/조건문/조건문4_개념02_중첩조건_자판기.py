'''
[키오스크]
	철수는 햄버거 가게를 운영한다.
	가게 내에 키오스크를 설치하고 잘 작동하는지 테스트하고 있다.
	랜덤으로 번호를 선택하고 아이템과 현금을 비교 후 결과를 출력하시오.

	해당 상품 가격이 현금보다 적으면, 현금에서 차감하고 구입 메세지를 출력하시오.
	해당 상품 가격이 현금보다 클 경우, "구입불가" 메세지를 출력하시오.
'''
import random

현금 = 3000
메뉴1 = 2500
메뉴2 = 3500

# 메뉴 출력
print("[키오스크]")
print("[1] 햄버거 2500원")
print("[2] 치킨조각 3500원")

# 번호 선택
print("번호를 입력하세요 : ")
select = random.randint(1, 2)
print("번호" , select , "을/를 선택하셨습니다.")

message = ''
change = 0
# 결과 출력
if select == 1:
    message += str(메뉴1) + '원인 햄버거를 구매하셨습니다.'
    change = 현금 - 메뉴1
else :
    message += str(메뉴2) + '원이 치킨조각를 구매하셨습니다.'
    change = 현금 - 메뉴2

if change > 0 :
    message += ' 거스름돈은 ' + str(change) + '입니다'
else :
    message += ' ' + str(abs(change)) + '원 부족하여 구입불가'
    
print(message)
    