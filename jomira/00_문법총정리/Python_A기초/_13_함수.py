# 파이썬 함수
# definition 정의
def test1():
    # pass
    print("함수호출!")
    
def test2(a,b):     # 매개변수(parameter)
    print(a+b)


num = 10
def test3():
    global num # 전역변수로 선언
    num = 3
    print("함수안의 num =",num) # 3
    

def test4(lst):
    lst[0] = 100

#--------------------------------------------
test1()
test2(10,20)   #인자,인수(argument)
test3()
print("함수밖의 num =",num) # 10
lst = [10,20,30,40,50]
test4(lst)
print(lst)
