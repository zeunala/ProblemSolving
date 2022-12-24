'''
모독

입력
첫 번째 줄에는 국회의원의 명수 N이 주어진다. (1 ≤ N ≤ 100,000)
이후 두 번째 줄부터 N개의 줄에 걸쳐 국회의원의 명예 점수가 주어지며,
그중 i번째 줄에는 i번째 국회의원의 명예점수인 정수 ai 가 주어진다. (1 ≤ ai ≤ 100,000)

출력
첫 번째 줄에 프로젝트를 성공시키기 위해 최소한으로 고용해야하는 해커의 수를 출력한다.
'''

'''
- 그리디 알고리즘으로 명예점수가 1인것부터 찾고, 없으면 만들어나가는 식으로 진행한다.
* Pass/1st/00:08:39
'''
import sys

N = int(sys.stdin.readline().rstrip())
arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort(reverse=True)

answer = 0
target = 1
while arr:
    # 명예점수가 지워질 수 있는걸 전부 지운다.
    isDeleted = False
    while arr and arr[-1] <= target:
        arr.pop()
        isDeleted = True
        
    # 만약 지워진게 하나도 없다면 지울걸 하나라도 만들어야한다.
    if isDeleted == False:
        answer += arr[-1] - target
        arr.pop()
        
    target += 1
    
print(answer)
    
    