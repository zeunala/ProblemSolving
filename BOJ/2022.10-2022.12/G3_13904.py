'''
과제

입력
첫 줄에 정수 N (1 ≤ N ≤ 1,000)이 주어진다.
다음 줄부터 N개의 줄에는 각각 두 정수 d (1 ≤ d ≤ 1,000)와 w (1 ≤ w ≤ 100)가 주어진다.
d는 과제 마감일까지 남은 일수를 의미하며, w는 과제의 점수를 의미한다.

출력
얻을 수 있는 점수의 최댓값을 출력한다.
'''

'''
- 마감일 남은 일수를 오름차순으로 정렬하고 과제들을 담을 최소힙을 만든다.
기존 최소힙의 최솟값보다 현재 과제의 w가 높고, 최소힙 원소의 개수가 d개이하라면 교체하는 방식으로 진행한다. 
* Pass/1st/00:07:41
'''
import heapq

N = int(input())
arr = []
for i in range(N):
    d, w = map(int, input().split())
    arr.append((d, w))
arr.sort()

target = [] # 과제들의 점수들이 담길 최소힙
for e in arr:
    d, w = e # d는 남은 일수, w는 과제의 점수
    
    if len(target) < d:
        heapq.heappush(target, w)
    else:
        if target[0] < w:
            heapq.heappushpop(target, w)

print(sum(target))