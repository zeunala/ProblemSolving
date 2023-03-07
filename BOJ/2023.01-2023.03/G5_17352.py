'''
여러분의 다리가 되어 드리겠습니다!

입력
첫 줄에 정수 N이 주어진다. (2 ≤ N ≤ 300,000)
그 다음 N - 2개의 줄에는 욱제가 무너뜨리지 않은 다리들이 잇는 두 섬의 번호가 주어진다.

출력
다리로 이을 두 섬의 번호를 출력한다. 여러 가지 방법이 있을 경우 그 중 아무거나 한 방법만 출력한다.
'''

'''
- 유니온 파인드를 이용하여 풀 수 있는 문제이다.
* Fail/1st/00:18:07
'''
import sys

def getParent(parent, i):
    while i != parent[i]:
        i = parent[i]
    parent[i] = i
    return i

N = int(sys.stdin.readline().rstrip())
parent = [i for i in range(N + 1)] # parent[i]는 i(i>=1)번과 연결된 섬의 번호로, 작은 번호가 우선된다.

for i in range(N - 2):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a > b: # a가 작은 수가 오도록 함
        a, b = b, a
    
    parent[b] = getParent(parent, a)

# 1번이 아닌 다른 섬이 끊긴 경우 그 섬은 parent[i] = i이며,
# 1번이 끊긴 경우 모든 섬에서 parent[i] = 1이다.
target = 1
for i in range(2, N + 1):
    if parent[i] == i:
        target = i
        break
    
if target == 1:
    print("1 2")
else:
    print("1 " + str(target))