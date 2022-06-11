'''
최대 힙

입력
첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고,
x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 자연수는 2^31보다 작다.

출력
입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.
'''

'''
- 파이썬의 heap을 사용하면 쉽게 계산할 수 있다.
* Pass/1st/00:03:38
'''
import heapq
import sys

N = int(sys.stdin.readline().rstrip())
arr = []

for i in range(N):
    commandNum = int(sys.stdin.readline().rstrip())
    
    if commandNum == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, -commandNum)