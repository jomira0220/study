'''
	[문제1]
		a리스트의 값들을 한 칸씩 
		앞으로 당기고 출력하시오.
	[정답1]
		a = [10,20,30,40,50,0]
  
	[문제2]
		b리스트의 값들을 한 칸씩 
		뒤로 밀고 출력하시오.
	[정답2]
		b =  [0,10,20,30,40,50]


# [문제1]
a = [0, 10, 20, 30, 40, 50]

for i in range(len(a)-1) :
    a[i] = a[i+1]
    
a[len(a)-1] = 0
print(a)
'''

# [문제2]
# [방법1]
b =  [10, 20, 30, 40, 50, 0]
temp = b[len(b)-1]
for i in range(len(b)-1,-1,-1):
    b[i] = b[i-1]
b[0] = temp
print(b)

# [방법2]
index = len(b) - 1
for i in range(len(b) - 1):
	b[index] = b[index - 1]
	index -= 1