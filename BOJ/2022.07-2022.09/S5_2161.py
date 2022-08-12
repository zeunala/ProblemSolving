'''
카드1

입력
첫째 줄에 정수 N(1 ≤ N ≤ 1,000)이 주어진다.

출력
첫째 줄에 버리는 카드들을 순서대로 출력한다. 제일 마지막에는 남게 되는 카드의 번호를 출력한다.
'''

'''
- N의 범위가 작으므로 문제를 그대로 구현하면 된다.
* Pass/1st/00:03:36
'''
from collections import deque

N = int(input())
tempDeque = deque()

for i in range(1, N + 1):
    tempDeque.append(i)
    
answer = ""
while tempDeque:
    answer += str(tempDeque.popleft()) + " "
    
    if tempDeque:
        tempDeque.append(tempDeque.popleft())
        
print(answer[:-1])