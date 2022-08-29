'''
풍선 터뜨리기

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000)이 주어진다.
다음 줄에는 차례로 각 풍선 안의 종이에 적혀 있는 수가 주어진다.
종이에 0은 적혀있지 않다.

출력
첫째 줄에 터진 풍선의 번호를 차례로 나열한다.
'''

'''
- N의 범위가 크지 않으므로 큐를 이용하여 직접 이동하는 방식을 사용해보도록 한다.
* Pass/1st/00:09:58
'''
from collections import deque

N = int(input())
arr = list(map(int, input().split()))

tempDeque = deque()
for i in range(len(arr)):
    tempDeque.append((i + 1, arr[i]))
    
answerArr = []
while tempDeque:
    (num, move) = tempDeque.popleft()
    answerArr.append(num)
    
    if not tempDeque:
        break
    
    if move > 0: # 오른쪽으로 이동
        for i in range(move - 1): # 큐 특성상 오른쪽으로 이동할 때는 1칸 덜 이동해야한다.
            temp = tempDeque.popleft()
            tempDeque.append(temp)
    else: # 왼쪽으로 이동
        for i in range(-move):
            temp = tempDeque.pop()
            tempDeque.appendleft(temp)

answer = ""
for e in answerArr:
    answer += str(e) + " "
print(answer[:-1])