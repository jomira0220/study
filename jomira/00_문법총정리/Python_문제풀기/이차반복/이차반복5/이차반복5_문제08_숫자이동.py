'''
	[문제]
		철수는 게임을 개발하고 있다.
		game리스트를 아래와 같이 사각형으로 출력한다.

		숫자8 은 현재 플레이어가 있는 자리이다.
		숫자0 은 플레이어가 이동할 수 있는 자리이다.
		숫자1 은 플레이어가 이동할 수 없는 벽이다.

		order리스트는 플레이어를 움직이기 위한 명령어들이다.
		숫자 1~4로 표현하고 북(1)동(2)남(3)서(4)를 뜻한다.

		order의 내용대로 플레이어가 이동하는 경로를 전부 출력하시오.
		벽 때문에 이동할 수 없을 때는 "이동 불가"를 출력하시오.
'''
game = [1,1,1,1,1,
	    1,0,0,0,1,
	    1,0,8,0,1,
	    1,0,0,0,1,
	    1,1,1,1,1]

order = [1,2,3,3,3,1,4,1]


position = 0
for i in range(len(game)) :
    if game[i] == 8 :
        position = i

print(f'position = {position}')


for i in range(len(order)) :
    
    temp = position
    
    if order[i] == 2 :
        position += 1
        print('동으로 이동!')
    if order[i] == 4 :
        position -= 1
        print('서으로 이동!')
    if order[i] == 3 :
        position += 5
        print('남으로 이동!')
    if order[i] == 1 :
        position -= 5    
        print('북으로 이동!')
        
    if game[position] == 1 :
        position = temp
        print('벽이다!')
    else :
        game[temp] = 0
        game[position] = 8
        
    for j in range(len(game)) :
        print(game[j],end='')
        if j % 5 == 4 :
            print()

    print()
    
    


        