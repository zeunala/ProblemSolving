'''
2+1 세일

입력
첫 번째 줄에는 유제품의 수 N (1 ≤ N ≤ 100,000)이 주어집니다.

두 번째 줄부터 N개의 줄에는 각 유제품의 가격 Ci (1 ≤ Ci ≤ 100,000)가 주어집니다.

출력
재현이가 N개의 유제품을 모두 살 때 필요한 최소비용을 출력합니다. 정답은 2^31-1보다 작거나 같다.
'''

'''
- 3개 묶음당 가장 싼 물건 하나가 무료이므로 그리디 알고리즘으로 풀면 된다.
* Pass/1st/00:02:52
'''
import sys

N = int(sys.stdin.readline().rstrip())
arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort(reverse=True)

answer = 0
for i in range(len(arr)):
    if i % 3 != 2: # 3n번째 물건은 무료
        answer += arr[i]
        
print(answer)