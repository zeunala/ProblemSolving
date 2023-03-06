'''
콘센트

입력
첫째 줄에 전자기기의 개수 N과 콘센트의 개수 M이 주어진다. (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10)
둘째 줄에 충전에 필요한 시간 ti를 나타내는 N개의 정수가 주어진다. (2^0 ​≤ ti ≤ 2^15, ti = 2^k (0 ≤ k ≤ 15, k는 정수))

출력
충전에 필요한 최소 시간을 출력한다.
'''

'''
- 충전에 필요한 시간이 2^k 꼴이므로 그리디 알고리즘으로 접근할 수 있다.
충전 시간을 내림차순으로 정렬하고 첫 번째 콘센트에 가장 긴 것을 충전한다.
그리고 그 다음 콘센트에는 그 다음으로 긴 것들을 첫 번째 콘센트 길이를 넘지 않도록 최대한 충전해서 넣고, 이를 반복한다.
예를 들어 8, 4, 4, 1, 1 이 있다면 8 / 4, 4 / 1, 1 과 같이 나눌 수 있다.
이게 가능한 이유는 2^k꼴로 정렬되어 있어 5 / 3 3과 같이 자리가 남는데 넣으면 초과되는 경우가 일어나지 않기 때문이다.
* Pass/1st/00:15:09
'''
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort(reverse=True)
totalTime = [0] * M # totalTime[i]는 i번째 콘센트로 충전하는 전자기기 들의 시간 총합

idx = 0 # 현재 몇 번째 콘센트를 가리키는지
for i in range(len(arr)):
    if idx == 0: # 첫 번째 콘센트에 남은 것중 가장 충전 시간이 긴 것을 넣는다.
        totalTime[idx] += arr[i]
        idx = (idx + 1) % M
        continue
    
    # 나머지 콘센트에는 이전 콘센트의 시간 총합을 넘지 않도록 최대한 넣는다.
    totalTime[idx] += arr[i]
    if totalTime[idx] == totalTime[idx - 1]:
        idx = (idx + 1) % M
    
print(totalTime[0]) # 첫 번째 콘센트가 가장 충전이 오래 걸리고 이 시간이 곧 총 충전 시간이다.