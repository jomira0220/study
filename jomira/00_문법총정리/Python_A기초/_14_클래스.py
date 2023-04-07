# 파이썬 클래스

def ex():
    pass

class Student:
    name = ""
    score = 0
    hakbun = 0
    def printInfo(self):
        print(self.name, self.score, self.hakbun)
    
#---------------------------------------
hgd = Student()
hgd.name = "홍길동"
hgd.score = 100
hgd.hakbun = 1001
hgd.printInfo()