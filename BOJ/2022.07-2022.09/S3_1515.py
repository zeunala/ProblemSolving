'''
수 이어 쓰기

입력
첫째 줄에 지우고 남은 수를 한 줄로 이어 붙인 수가 주어진다.
이 수는 최대 3,000자리다.

출력
가능한 N 중에 최솟값을 출력한다.
'''

'''
- 입력으로 주어진 숫자의 길이가 3000이므로 맨 앞에서부터 읽어가며 숫자 몇의 일부인지 순서대로 따져보도록 한다.
* Pass/1st/00:09:45
'''
inputString = input()
inputIdx = 0 # inputString[0]부터 차례대로 읽어간다

answer = 0

# answer를 1부터 늘려가며 inputString과 맞는 부분이 나올때까지 증가시킨다.
while inputIdx < len(inputString):
    answer += 1
    
    currentString = str(answer)
    currentIdx = 0
    while currentIdx < len(currentString):
        if currentString[currentIdx] == inputString[inputIdx]:
            inputIdx += 1
            currentIdx += 1
        else:
            currentIdx += 1
        
        if inputIdx >= len(inputString): # 중간에 입력값을 모두 읽었다면 탈출
            break
    
    
    
print(answer)
            