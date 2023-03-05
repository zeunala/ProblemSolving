'''
녹색 옷 입은 애가 젤다지?

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스의 첫째 줄에는 동굴의 크기를 나타내는 정수 N이 주어진다. (2 ≤ N ≤ 125) N = 0인 입력이 주어지면 전체 입력이 종료된다.
이어서 N개의 줄에 걸쳐 동굴의 각 칸에 있는 도둑루피의 크기가 공백으로 구분되어 차례대로 주어진다.
도둑루피의 크기가 k면 이 칸을 지나면 k루피를 잃는다는 뜻이다. 여기서 주어지는 모든 정수는 0 이상 9 이하인 한 자리 수다.

출력
각 테스트 케이스마다 한 줄에 걸쳐 정답을 형식에 맞춰서 출력한다. 형식은 예제 출력을 참고하시오.
'''

'''
- 시작점에서의 거리를 각 칸마다 저장하여 처음 가장 짧은 칸부터 인접한 칸을 방문하는 식으로 계산한다.
* Pass/1st/00:22:32
'''
import sys
import heapq

INF = 10 ** 10
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def getMinCost(arr, n):
    costArr = [[INF for _ in range(n)] for _ in range(n)] # 시작점에서의 거리
    
    tempHeap = [] # 시작점에서의 거리와 좌표가 담긴 우선순위 큐
    heapq.heappush(tempHeap, (arr[0][0], 0, 0))
    
    while tempHeap:
        currentCost, currentI, currentJ = heapq.heappop(tempHeap)
        if currentI == n - 1 and currentJ == n - 1:
            return currentCost
        if costArr[currentI][currentJ] <= currentCost:
            continue
        costArr[currentI][currentJ] = currentCost
        
        for i in range(len(di)):
            nextI = currentI + di[i]
            nextJ = currentJ + dj[i]
            if nextI >= 0 and nextJ >= 0 and nextI < n and nextJ < n:
                if costArr[nextI][nextJ] > currentCost + arr[nextI][nextJ]:
                    heapq.heappush(tempHeap, (currentCost + arr[nextI][nextJ], nextI, nextJ))
                    
problemNo = 1
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
        
    print("Problem " + str(problemNo) + ": " + str(getMinCost(arr, n)))
    problemNo += 1