'''
부분수열의 합 2

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 40, |S| ≤ 1,000,000)
둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.
'''

'''
- 음수가 있으므로 투포인터로는 어려워보이며, N의 범위가 작으므로 모든 범위를 계산해보도록 한다.
* Fail/1st/00:05:51
- 문제를 연속된 부분순열로 잘못 알고 풀이하였다. N이 최대 40이므로 우선 둘로 나누어 가능한 모든 합의 경우들을 저장해놓고,
이후 두 집합에서 합이 S가 되는 경우의 수를 구해보도록 접근해보자.
* Pass/2nd/00:26:46
'''
from collections import defaultdict
from copy import deepcopy

N, S = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

arrPart1 = arr[:len(arr) // 2]
arrPart2 = arr[len(arr) // 2:]

arrSumPart1 = defaultdict(int)
arrSumPart2 = defaultdict(int)

arrSumPart1[0] = 1 # 아무것도 안 고른 경우
arrSumPart2[0] = 1

# 모든 arrSumPart1에 대해 arrPart1 원소 값을 더한 경우를 추가한다. (더하지 않은 경우와 더한 경우 두 가지 경우가 존재하게 된다)
for e in arrPart1:
    temp = deepcopy(arrSumPart1)
    for e2 in temp.keys():
        arrSumPart1[e2 + e] += temp[e2]
        
for e in arrPart2:
    temp = deepcopy(arrSumPart2)
    for e2 in temp.keys():
        arrSumPart2[e2 + e] += temp[e2]
        
# arrPart1에서 나올 수 있는 모든 합의 경우의 수와, arrPart2에서 나올 수 있는 모든 합의 경우의 수를 조합한다.
for e in arrSumPart1.keys():
    if S - e in arrSumPart2:
        answer += arrSumPart1[e] * arrSumPart2[S - e]

if S == 0:  # 각각 아무것도 고르지 않는 경우가 들어가서는 안되므로 빼줘야한다.
    answer -= 1
    
print(answer)