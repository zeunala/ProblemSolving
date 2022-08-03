'''
카드

입력
첫째 줄에 준규가 가지고 있는 숫자 카드의 개수 N (1 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N개 줄에는 숫자 카드에 적혀있는 정수가 주어진다.

출력
첫째 줄에 준규가 가장 많이 가지고 있는 정수를 출력한다.
'''

'''
- 딕셔너리를 이용하여 쉽게 구할 수 있다.
* Pass/1st/00:05:38
'''
from collections import defaultdict
import sys

dict = defaultdict(int)
N = int(sys.stdin.readline().rstrip())

# 입력받은 숫자로 딕셔너리 만듦
for i in range(N):
    dict[int(sys.stdin.readline().rstrip())] += 1
    
maxValue = max(dict.values()) # 가장 많이 나온 수의 등장 횟수
dictKeys = list(dict.keys())
dictKeys.sort()

# 가장 많이 나온 수 중 최솟값을 찾음
for e in dictKeys:
    if dict[e] == maxValue:
        print(e)
        break