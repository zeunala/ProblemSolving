'''
소수 경로

입력
첫 줄에 test case의 수 T가 주어진다. 다음 T줄에 걸쳐 각 줄에 1쌍씩 네 자리 소수가 주어진다.

출력
각 test case에 대해 두 소수 사이의 변환에 필요한 최소 회수를 출력한다. 불가능한 경우 Impossible을 출력한다.
'''

'''
- 일단 1000~9999까지 소수들을 다 구해보고, 변환할 수 있는 수 끼리 연결해서 그래프를 만들어보자.
그렇다면 주어진 두 점 사이의 최소 경로 길이를 찾는 문제로 바뀌게 된다.
* Pass/1st/00:35:26
'''
import sys
from queue import deque

def bfs(graph, start, end):
    bfsQueue = deque() # 정점과 현재까지 이동거리의 튜플이 저장된다.
    visited = [False] * 10000
    bfsQueue.append((start, 0))
    
    while bfsQueue:
        (a, b) = bfsQueue.popleft()
        if visited[a]:
            continue
        else:
            visited[a] = True
            if a == end:
                return b
        
        for e in graph[a]:
            if visited[e]:
                continue
            else:
                bfsQueue.append((e, b + 1))
            
    return "Impossible"
        
N = int(input())
inputArr = []
isPrime = [True] * 10000 # isPrime[a]는 a가 소수인지 여부를 알려준다.
primeGraph = [[] for _ in range(10000)] # 소수끼리 연결된 graph
for i in range(N):
    inputArr.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(1000): # 1000이상만 허용하므로 999까지는 소수이더라도 False로 처리한다.
    isPrime[i] = False
    
for i in range(2, 101):
    for j in range(1, (10001//i)+1):
        if i*j < 10000:
            isPrime[i*j] = False

for i in range(1000, 10000):
    for j in range(10):
        temp1 = i - (i // 1000 * 1000) + (1000 * j) # i에서 첫번째 자리를 교체 한 것
        temp2 = i - (i % 1000 // 100 * 100) + (100 * j)
        temp3 = i - (i % 100 // 10 * 10) + (10 * j)
        temp4 = i - (i % 10) + j
        
        if temp1 != i and isPrime[temp1]:
            primeGraph[i].append(temp1)
        if temp2 != i and isPrime[temp2]:
            primeGraph[i].append(temp2)
        if temp3 != i and isPrime[temp3]:
            primeGraph[i].append(temp3)
        if temp4 != i and isPrime[temp4]:
            primeGraph[i].append(temp4)

for i in range(N):
    print(bfs(primeGraph, inputArr[i][0], inputArr[i][1]))