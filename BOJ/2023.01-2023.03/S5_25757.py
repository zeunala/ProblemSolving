'''
임스와 함께하는 미니게임

입력
첫 번째 줄에는 사람들이 임스와 같이 플레이하기를 신청한 횟수 N과 같이 플레이할 게임의 종류가 주어진다. (1 <= N <= 100000)
두 번째 줄부터 N개의 줄에는 같이 플레이하고자 하는 사람들의 이름이 문자열로 주어진다. (1 <= 문자열 길이 <= 20)
사람들의 이름은 숫자 또는 영문 대소문자로 구성되어 있다.

출력
임스가 최대로 몇 번이나 게임을 플레이할 수 있는지 구하시오.
'''

'''
- 파이썬의 집합 자료형으로 서로 다른 사람들을 구하고 그에 따라 게임을 최대 몇 번까지 할 수 있는지 계산한다.
* Pass/1st/00:05:42
'''
import sys

N, playType = sys.stdin.readline().rstrip().split()
N = int(N)

people = set()

for i in range(N):
    people.add(sys.stdin.readline().rstrip())
    
if playType == "Y": # 윷놀이(2명)는 서로 다른 사람 1명당 게임 1번 가능
    print(len(people))
elif playType == "F": # 같은 그림 찾기(3명)는 2명당 1번
    print(len(people) // 2)
elif playType == "O": # 원카드(4명)는 3명당 1번
    print(len(people) // 3)