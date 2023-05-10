'''
로또

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있다.
첫 번째 수는 k (6 < k < 13)이고, 다음 k개 수는 집합 S에 포함되는 수이다.
S의 원소는 오름차순으로 주어진다.
입력의 마지막 줄에는 0이 하나 주어진다. 

출력
각 테스트 케이스마다 수를 고르는 모든 방법을 출력한다. 이때, 사전 순으로 출력한다.
각 테스트 케이스 사이에는 빈 줄을 하나 출력한다.
'''

'''
- 파이썬의 combinations로 간단하게 계산할 수 있다.
* Fail/1st/00:04:50
- 테스트 케이스 사이에 빈 줄을 하나 출력하라는 조건을 놓쳐 관련 코드를 추가하였다.
* Pass/2nd/00:05:20
'''
import sys
from itertools import combinations

while True:
    inputArr = list(map(int, sys.stdin.readline().rstrip().split())) # 오름차순 정렬된 상태
    PICK_COUNT = 6
    
    if inputArr[0] == 0:
        break
    
    for case in combinations(inputArr[1:], PICK_COUNT):
        for e in case:
            print(e, end = " ")
        print()
    print()