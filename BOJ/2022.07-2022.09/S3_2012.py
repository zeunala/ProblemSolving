'''
등수 매기기

입력
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 500,000)
둘째 줄부터 N개의 줄에 걸쳐 각 사람의 예상 등수가 순서대로 주어진다.
예상 등수는 500,000 이하의 자연수이다.

출력
첫째 줄에 불만도의 합을 최소로 할 때, 그 불만도를 출력한다.
'''

'''
- 예상 등수를 오름차순으로 정렬하고 예상 등수가 높은 것부터 1등, 2등, ... 식으로 부여하도록 한다.
* Pass/1st/00:06:15
'''
import sys

N = int(sys.stdin.readline().rstrip())
arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
    
arr.sort()

answer = 0
for i in range(N):
    answer += abs((i + 1) - arr[i])

print(answer)