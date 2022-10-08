'''
사이클 단어

입력
첫째 줄에 단어의 개수 N이 주어진다.
둘째 줄부터 단어가 한 줄에 하나씩 주어진다.
단어는 영어 소문자로만 이루어져 있다.
N은 50보다 작거나 같은 자연수이며, 단어의 길이는 최대 50이다.

출력
첫째 줄에 서로 다른 단어가 몇 개인지 출력한다.
'''

'''
- 단어의 길이가 작으므로 모든 경우의 수를 집합에 넣는 식으로 구현한다.
* Pass/1st/00:04:45
'''
N = int(input())
answer = 0

currentSet = set() # 단어를 넣을 때마다 모든 사이클 경우의 수를 넣는다.

for i in range(N):
    currentWord = input()
    
    if currentWord in currentSet:
        pass
    else:
        answer += 1
        # 사이클의 경우의 수를 모두 따진다.
        for i in range(len(currentWord)):
            currentSet.add(currentWord[i:] + currentWord[:i])

print(answer)