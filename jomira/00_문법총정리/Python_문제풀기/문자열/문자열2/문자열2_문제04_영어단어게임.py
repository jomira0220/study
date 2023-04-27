'''
    [문제]
        철수는 영어단어 타자 게임을 만들고 있다.
        한 단어씩 출력하는데 그냥 출력하면 재미없기 때문에 
        랜덤 위치에 글자 대신 * 을 한 개 출력한다.
        타자 게임을 구현을 위한 화면을 출력하시오.
    [예시]
        ja*a
        pytho*
        c+*
        n*de
        *avascript
'''
wordList = ["java", "python", "c++", "node", "javascript"]

import random
for i in range(len(wordList)):
    index = random.randint(0,len(wordList[i])-1)
    temp = ''
    for j in range(len(wordList[i])):
        if j == index :
            temp += '*'
        else :
            temp += wordList[i][j]
    wordList[i] = temp
    
print(wordList)
    