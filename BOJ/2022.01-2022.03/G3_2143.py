'''
두 배열의 합

입력
첫째 줄에 T(-1,000,000,000 ≤ T ≤ 1,000,000,000)가 주어진다.
다음 줄에는 n(1 ≤ n ≤ 1,000)이 주어지고, 그 다음 줄에 n개의 정수로 A[1], …, A[n]이 주어진다.
다음 줄에는 m(1 ≤ m ≤ 1,000)이 주어지고, 그 다음 줄에 m개의 정수로 B[1], …, B[m]이 주어진다.
각각의 배열 원소는 절댓값이 1,000,000을 넘지 않는 정수이다.

출력
첫째 줄에 답을 출력한다. 가능한 경우가 한 가지도 없을 경우에는 0을 출력한다.
'''

'''
- 배열의 크기가 크지 않으므로 가능한 B 부배열 합을 모두 구해놓고, 모든 A 경우에 대해 체크해보자.
이 때 0이 있을 수 있음에 주의하자.
* Pass/1st/00:46:30
'''
import sys
from collections import Counter

T = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
B = list(map(int, sys.stdin.readline().rstrip().split()))

answer = 0

allB = []
for i in range(m):
    currentBSum = 0
    for j in range(i, m):
        currentBSum += B[j]
        allB.append(currentBSum)
        
allBCounter = Counter(allB)

for i in range(n):
    currentASum = 0
    for j in range(i, n):
        currentASum += A[j]
        answer += allBCounter[T-currentASum]
    
print(answer)
