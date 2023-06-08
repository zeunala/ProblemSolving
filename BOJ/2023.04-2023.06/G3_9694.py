'''
무엇을 아느냐가 아니라 누구를 아느냐가 문제다

입력
맨위 첫 번째 줄에 T(1 <T< 100)는 테스트케이스 수를 의미한다.
이것을 따라 다음줄에 각 테스트 케이스가 주어지는데, 첫 번째 줄에는 N과 M이 주어진다.
N(N ≤ 20)은 관계의 개수를 의미하며, M(5 ≤M≤ 20)은 정치인의 수를 나타낸다.
이 다음 N줄에는 정치인 x, 그의 친구 y (0 ≤x,y< M), 두사람간의 친밀도 z(1 ≤z≤ 4)를 입력받는다.
정치인 0번은 한신이를 나타내고 M-1은 최고의원을 의미한다.

출력
각 테스트 케이스는 "Case #x: "의 형식으로 출력되며 x는 케이스 번호(1부터 시작)을 의미한다.
콜론뒤에 한신이가 최고의원을 만날수 있다면 0번 정치인(한신이)를 시작으로 M-1번 정치인(최고의원)까지 만난 순서대로 출력하면 되고,
최고의원을 만날수 없는 경우엔 -1을 출력하면 된다.
'''

'''
- 다익스트라 알고리즘을 이용하여 풀 수 있다.
* Fail/1st/00:17:18
- 알고리즘 코드를 수정하였다.
* Pass/2nd/00:23:31
'''
import heapq

def solution(graph):
    M = len(graph)
    INF = 10 ** 10
    
    minArr = [INF] * M # minArr[i]는 i번 정치인까지 가는 최소 비용
    tempHeap = [] # (minArr[i], i)의 최소힙
    parent = [None] * M # parent[i]는 최단경로로 이동했을 때 i직전에 이동하는 번호
    
    minArr[0] = 0
    heapq.heappush(tempHeap, (0, 0))
    
    while tempHeap:
        cost, start = heapq.heappop(tempHeap)
        if minArr[start] < cost:
            continue
        
        for next in graph[start].keys():
            if minArr[next] > minArr[start] + graph[start][next]:
                minArr[next] = minArr[start] + graph[start][next]
                parent[next] = start
                
                heapq.heappush(tempHeap, (minArr[next], next))
    
    if minArr[M - 1] == INF:
        return "-1"
    else:
        answer = ""
        current = M - 1
        while current != None:
            answer = str(current) + " " + answer
            current = parent[current]
        return answer

T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    graph = [dict() for _ in range(M)]
    
    for i in range(N):
        x, y, z = map(int, input().split())
        graph[x][y] = z
        graph[y][x] = z
        
    print("Case #{0}: {1}".format(case + 1, solution(graph)))