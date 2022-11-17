'''
중앙값 구하기

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
각 테스트 케이스의 첫째 줄에는 수열의 크기 M(1 ≤ M ≤ 9999, M은 홀수)이 주어지고,
그 다음 줄부터 이 수열의 원소가 차례대로 주어진다.
원소는 한 줄에 10개씩 나누어져있고, 32비트 부호있는 정수이다.

출력
각 테스트 케이스에 대해 첫째 줄에 출력하는 중앙값의 개수를 출력하고,
둘째 줄에는 홀수 번째 수를 읽을 때 마다 구한 중앙값을 차례대로 공백으로 구분하여 출력한다.
이때, 한 줄에 10개씩 출력해야 한다.
'''

'''
- 중앙값을 빠른 시간 안에 구해야 하는 문제이다.
최대힙과 최소힙을 하나씩 두어 각각 n/n 또는 n+1/n개의 원소를 갖도록 한다.
* Pass/1st/00:13:31
'''
import sys
import heapq

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    M = int(sys.stdin.readline().rstrip())
    arr = []
    answer = []
    
    for j in range((M - 1)// 10 + 1):
        arr += list(map(int, sys.stdin.readline().rstrip().split()))
        
    # 원소를 반반씩 갖되 왼쪽 힙의 모든 원소는 오른쪽 힙의 모든 원소보다 작도록 유지하면 왼쪽 힙의 최댓값이 중앙값이 된다.
    leftMaxHeap = []
    rightMinHeap = []
    
    for j in range(M):
        # 왼쪽 힙, 오른쪽 힙 순서대로 하나씩 넣고, 왼쪽 힙의 최댓값 > 오른쪽 힙의 최솟값이라면 하나씩 교체한다.
        if j % 2 == 0:
            heapq.heappush(leftMaxHeap, -arr[j])
        else:
            heapq.heappush(rightMinHeap, arr[j])
            
        if rightMinHeap and (-leftMaxHeap[0] > rightMinHeap[0]):
            temp1 = -heapq.heappop(leftMaxHeap)
            temp2 = heapq.heappop(rightMinHeap)
            heapq.heappush(leftMaxHeap, -temp2)
            heapq.heappush(rightMinHeap, temp1)
        
        # 중앙값 저장
        if j % 2 == 0:
            answer.append(-leftMaxHeap[0])
    
    print(len(answer))
    for j in range(len(answer)):
        if j % 10 == 9 or j == len(answer) - 1:
            print(answer[j])
        else:
            print(answer[j], end = " ")