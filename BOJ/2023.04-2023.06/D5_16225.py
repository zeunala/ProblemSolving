'''
제271회 웰노운컵

입력
첫 줄에 짝수 N(2 ≤ N ≤ 200,000)이 주어진다.
다음 줄에 A[1], ..., A[N], 그 다음 줄에 B[1], ..., B[N]이 (1 ≤ A[i], B[i] ≤ 109) 주어진다.
모든 A[i]는 서로 다르고, 모든 B[i]도 서로 다르다.

출력
내가 가져가는 문제의 A[i]값의 최대 합을 출력한다.
'''

'''
- 우선 B를 내림차순으로 정렬했을 때 각각의 A값들을 나열한다.
A값들을 최대힙으로 담아서 각 B값에 대해 하나씩 꺼내서 매칭시킨다.
단, 이미 꺼낸 적이 있는 B값에 대응하는 A값은 제외해야 하며, 모든 A와 B값들은 모두 다르다는 점도 이용한다.
* Fail/1st/00:29:37
'''
import sys
import heapq

N = int(sys.stdin.readline().rstrip())
arrA = list(map(int, sys.stdin.readline().rstrip().split()))
arrB = list(map(int, sys.stdin.readline().rstrip().split()))
arrBA = [] # (B[i], A[i]) 들의 배열

for i in range(N):
    arrBA.append((arrB[i], arrA[i]))
arrBA.sort(reverse = True)

heapA = [(-arrA[i], -arrB[i]) for i in range(N)] # (A값, B값) 들이 담긴 최대힙
heapq.heapify(heapA)

answer = 0
visitedA = set() # 이미 꺼낸 적이 있는 B값에 대응하는 A값, 이 값들은 점수를 얻지 못함
visitedB = set() # 이미 꺼낸 B값

bIdx = 0
for i in range(N // 2): # 총 N/2번 체크
    while arrBA[bIdx][0] in visitedB: # 이미 꺼낸 B값은 체크하지 않음
        bIdx += 1
    visitedA.add(arrBA[bIdx][1])
    
    tempA, tempB = heapq.heappop(heapA)
    tempA, tempB = -tempA, -tempB
    while tempA in visitedA:
        tempA, tempB = heapq.heappop(heapA)
        tempA, tempB = -tempA, -tempB
    visitedB.add(tempB)
    answer += tempA
    
    bIdx += 1
print(answer)