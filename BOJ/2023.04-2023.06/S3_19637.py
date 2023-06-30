'''
IF문 좀 대신 써줘

입력
첫 번째 줄에는 칭호의 개수 N (1 ≤ N ≤ 10^5)과
칭호를 출력해야 하는 캐릭터들의 개수 M (1 ≤ M ≤ 10^5)이 빈칸을 사이에 두고 주어진다. (1 ≤ N, M ≤ 10^5)
두 번째 줄부터 N개의 줄에 각 칭호의 이름을 나타내는 길이 1 이상, 11 이하의 영어 대문자로만 구성된 문자열과
해당 칭호의 전투력 상한값을 나타내는 10^9 이하의 음이 아닌 정수가 주어진다. 칭호는 전투력 상한값의 비내림차순으로 주어진다. 
N + 2번째 줄부터 M개의 각 줄에는 캐릭터의 전투력을 나타내는 음이 아닌 정수가 주어진다.
해당하는 칭호가 없는 전투력은 입력으로 주어지지 않는다.

출력
M개의 줄에 걸쳐 캐릭터의 전투력에 맞는 칭호를 입력 순서대로 출력한다.
어떤 캐릭터의 전투력으로 출력할 수 있는 칭호가 여러 개인 경우 가장 먼저 입력된 칭호 하나만 출력한다.
'''

'''
- 파이썬의 bisect_left를 이용해서 X보다 작은 가장 큰 카테고리를 O(logN)에 찾도록 한다.
* Pass/1st/00:07:23
'''
import sys
from bisect import bisect_left

powerArr = []
nameArr = [] # nameArr[i]는 powerArr[i]이하에 해당하는 power값의 이름에 해당한다.
visited = set() # 중복 전투력값 삭제

N, M = map(int, sys.stdin.readline().rstrip().split())
for i in range(N):
    name, power = sys.stdin.readline().rstrip().split()
    power = int(power)
    
    if power in visited:
        continue
    visited.add(power)
    
    powerArr.append(power)
    nameArr.append(name)
    
for i in range(M):
    power = int(sys.stdin.readline().rstrip())
    print(nameArr[bisect_left(powerArr, power)])