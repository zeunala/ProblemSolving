'''
줄 세우기

입력
첫째 줄에 N(1 ≤ N ≤ 32,000), M(1 ≤ M ≤ 100,000)이 주어진다.
M은 키를 비교한 회수이다.
다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다.
이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.
학생들의 번호는 1번부터 N번이다.

출력
첫째 줄에 학생들을 키 순서대로 줄을 세운 결과를 출력한다.
답이 여러 가지인 경우에는 아무거나 출력한다.
'''

'''
- 위상 정렬 문제로 보인다. 시간초과가 나지 않도록 조심해서 작성한다.
* Pass/1st/00:16:46
'''
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
arrFront = [[] for _ in range(N)] # i번(0~N-1) 사람이 누구 앞에 서야하는지를 나타낸다.
arrBehind = [[] for _ in range(N)] # i번(0~N-1) 사람이 누구 뒤에 서야하는지를 나타낸다.
for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arrFront[a - 1].append(b - 1)
    arrBehind[b - 1].append(a - 1)

nodeQueue = deque() # 누구 뒤에 서야하는지에 대한 조건이 없는 학생들이 여기 담김
result = "" # 줄을 세운 결과 (이 때 1을 더해 1~N번의 사람이 되도록 바꿔줘야 한다)

for i in range(N):
    if len(arrBehind[i]) == 0:
        nodeQueue.append(i)

while nodeQueue:
    currentNode = nodeQueue.popleft()
    result += (str(currentNode + 1) + " ")
    
    for e in arrFront[currentNode]: # arrBehind에서 빠져나간 노드를 제거
        arrBehind[e].remove(currentNode)
        if len(arrBehind[e]) == 0:
            nodeQueue.append(e)
        

print(result[:-1]) # 마지막 공백 제거