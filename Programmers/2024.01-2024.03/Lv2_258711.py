'''
도넛과 막대 그래프

- 우선 새로 추가한 정점의 번호부터 찾는다. 나가는게 2개 이상이면서 들어오는게 하나도 없는 점이다.
도넛모양은 DFS나 BFS로 계속 탐색하면 원래대로 돌아온다.
막대모양은 계속 탐색하면 멈춘다.
8자모양은 계속 탐색하다가 2개로 뻗어나가는 곳이 존재한다.

* Pass/1st/00:17:21
'''
def check(graph, e): # check(graph, e)는 도넛 1, 막대 2, 8자 3을 리턴한다.
    visited = set()
    visited.add(e)
    
    current = e
    while True:
        if len(graph[current]) == 0: # 멈췄으면 막대
            return 2
        if len(graph[current]) == 2: # 나갈 곳이 2개면 8자
            return 3
        current = graph[current][0]
        if current in visited: # 이미 방문한 곳을 또 방문하면 도넛
            return 1
        visited.add(current)
    

def solution(edges):
    answer = [0, 0, 0, 0] # 정점 번호, 도넛, 막대, 8자
    
    graph = [[] for _ in range(1000001)]
    graphOut = [0] * 1000001 # graphOut[i]는 i에서 나오는 점의 개수
    graphIn = [0] * 1000001 # graphIn[i]는 i로 들어가는 점의 개수
    allDot = set() # 존재하는 정점 번호들
    
    for edge in edges:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graphOut[a] += 1
        graphIn[b] += 1
        allDot.add(a)
        allDot.add(b)
        
    start = 10 ** 10
    for dot in allDot:
        if graphOut[dot] >= 2 and graphIn[dot] == 0:
            start = dot
            break
    
    answer[0] = start
    
    for e in graph[start]:
        answer[check(graph, e)] += 1 # check(graph, e)는 도넛 1, 막대 2, 8자 3을 리턴한다.
    
    return answer