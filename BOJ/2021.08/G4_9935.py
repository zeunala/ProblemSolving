'''
문자열 폭발

입력
첫째 줄에 문자열이 주어진다. 문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다.
둘째 줄에 폭발 문자열이 주어진다. 길이는 1보다 크거나 같고, 36보다 작거나 같다.
두 문자열은 모두 알파벳 소문자와 대문자, 숫자 0, 1, ..., 9로만 이루어져 있다.

출력
첫째 줄에 모든 폭발이 끝난 후 남은 문자열을 출력한다.
'''

'''
- 파이썬의 replace를 반복해서 호출하면 될 것으로 생각하였으나 문자열이 100만까지라 "a"*500000+"b"*500000, "ab" 같은 경우 시간이 너무 걸린다.
O(N)의 알고리즘이 되도록 문자열 처음부터 쭉 지나가서 검사하는 식으로 구현하였다.
* Fail/1st/00:35:08/TimeOver
- 문자열 슬라이싱 하는 것에서 시간이 오래 걸리는 것으로 추정되어 이를 개선해야 할 것이다.
* Pass/2nd/01:45:30(use PyPy3)
- Python으로는 시간초과가 떴으나 PyPy3으로 채점할 때는 맞은 것으로 보아 최적화가 좀 더 필요한 것으로 보인다.
실패함수를 이용하는 방법 등을 사용하여 문자열 탐색 시간을 줄일 수 있을 것이다.
- 이후 다른 사람들의 답안을 참고한 결과 answer를 스택으로 두고, inputString을 탐색하면서 answer에 쌓되 bombString의 마지막 문자를 만나는 경우
기존 answer스택을 체크하여 폭발시키는 방법을 볼 수 있었다. 이 방법을 쓰면 inputString을 되돌아가지 않아도 되므로 더 빠르고 간편할 것이다.
'''
import sys

inputString = sys.stdin.readline().rstrip()
bombString = sys.stdin.readline().rstrip()
answer = [""]*len(inputString)
answerIdx = 0 # 문자열 폭발로 인덱스를 되돌아갈때 사용
answerLen = 0


i = 0
while i < len(inputString):
    if i >= len(inputString)-(len(bombString)-1)+(answerLen-answerIdx):
        answer[answerLen] = inputString[i]
        answerIdx += 1
        answerLen += 1
        i += 1
        continue

    bomb = True
    for j in range(len(bombString)):
        if answerIdx+j < answerLen:
            if answer[answerIdx+j] != bombString[j]:
                bomb = False
                break
        else:
            if inputString[i+j-(answerLen-answerIdx)] != bombString[j]:
                bomb = False
                break

    if bomb:
        if answerIdx < answerLen: # 폭발 문자열이 answer와 inputString에 걸쳐있을 경우
            i += len(bombString)-(answerLen-answerIdx)
            answerLen = answerIdx
            answerIdx -= len(bombString)-1 # 기존 answer에서 또 터질 수 있으므로 체크
            if answerIdx < 0:
                answerIdx = 0
        else: # 폭발 문자열이 inputString에만 존재하는 경우
            i += len(bombString)
            answerIdx -= len(bombString)-1 # 기존 answer에서 또 터질 수 있으므로 체크
            if answerIdx < 0:
                answerIdx = 0
    else:
        if answerIdx < answerLen: # 폭발해서 answer를 되돌아가서 체크 중일 경우
            answerIdx += 1
        else:
            answer[answerLen] = inputString[i]
            answerIdx += 1
            answerLen += 1
            i += 1

if answerLen == 0:
    print("FRULA")
else:
    for i in range(answerLen):
        print(answer[i], end="")
    print()
        
