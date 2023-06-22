'''
숫자 야구

입력
첫째 줄에는 민혁이가 영수에게 몇 번이나 질문을 했는지를 나타내는 1 이상 100 이하의 자연수 N이 주어진다.
이어지는 N개의 줄에는 각 줄마다 민혁이가 질문한 세 자리 수와 영수가 답한 스트라이크 개수를 나타내는 정수와 볼의 개수를 나타내는 정수,
이렇게 총 세 개의 정수가 빈칸을 사이에 두고 주어진다.

출력
첫 줄에 영수가 생각하고 있을 가능성이 있는 답의 총 개수를 출력한다.
'''

'''
- N의 숫자의 범위가 적으므로 가능한 모든 숫자를 대상으로 질문 N개의 답을 모두 만족하는 숫자들의 개수를 세도록 한다.4
* Pass/1st/00:09:14
'''
import sys
from itertools import permutations

def isValid(target, num, strike, ball):
    a, b, c = target // 100, (target % 100) // 10, target % 10
    answerA, answerB, answerC = num // 100, (num % 100) // 10, num % 10
    
    answerStrike = 0
    answerBall = 0
    
    if a == answerA:
        answerStrike += 1
    if b == answerB:
        answerStrike += 1
    if c == answerC:
        answerStrike += 1
        
    if a == answerB or a == answerC:
        answerBall += 1
    if b == answerA or b == answerC:
        answerBall += 1
    if c == answerA or c == answerB:
        answerBall += 1
        
    return answerStrike == strike and answerBall == ball

N = int(sys.stdin.readline().rstrip())
question = [] # (세자리 수, 스트라이크 수, 볼 수)의 배열

for i in range(N):
    question.append(tuple(map(int, sys.stdin.readline().rstrip().split())))
    
answer = 0
for case in permutations(range(1, 10), 3): # 1~9로 구성된 서로 다른 세 가지의 수
    # (1, 2, 3)과 같을 꼴을 123의 세자리 정수(target)로 변환
    a, b, c = case
    target = 100 * a + 10 * b + c
    
    result = True # 질문들을 모두 만족하는지
    for (num, strike, ball) in question:
        if not isValid(target, num, strike, ball):
            result = False
            break
        
    if result:
        answer += 1
print(answer)