'''
수들의 합 4

입력
첫째 줄에 정수 N과 K가 주어진다. (1 ≤ N ≤ 200,000, |K| ≤ 2,000,000,000) N과 K 사이에는 빈칸이 하나 있다.
둘째 줄에는 배열 A를 이루는 N개의 정수가 빈 칸을 사이에 두고 A[1], A[2], ..., A[N]의 순서로 주어진다.
주어지는 정수의 절댓값은 10,000을 넘지 않는다.

출력
첫째 줄에 합이 K인 부분합의 개수를 출력한다.
'''

'''
- A[i]~A[j]까지의 부분합을 A[i, j]라고 한다면, A[i, j] = A[1, j] - A[1, i - 1]이다. (단, A[1, 0] = 0)
따라서 A[1, j]에서 j를 1부터 증가시켜가며 A[1, i - 1]을 뺐을 때 K가 되는 개수를 더해나간다.
* Pass/1st/00:12:49
'''
import sys
from collections import defaultdict

N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

answer = 0
prevResults = defaultdict(int) # A[1, i - 1]의 값들 (j를 1부터 증가시켜나갈 때 A[1, j]값을 구하고 이전값들을 여기에 담음)
prevResults[0] += 1 # A[1, 0] = 0의 경우를 추가
currentSum = 0 # 현재 A[1, j]의 값 (j를 1부터 증가시켜나감)
for i in range(len(arr)):
    currentSum += arr[i]
    
    if currentSum - K in prevResults: # A[1, j] - A[1, i - 1] = K가 되는 A[1, i - 1]값이 존재하는지
        answer += prevResults[currentSum - K]
    prevResults[currentSum] += 1
    
print(answer)