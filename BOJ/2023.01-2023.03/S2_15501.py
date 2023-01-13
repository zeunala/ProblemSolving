'''
부당한 퍼즐

입력
첫째 줄에 n이 주어진다(1 ≤ n ≤ 1,000,000).
둘째 줄에 1에서 n까지의 수가 한 번만 나타나는 수열이 순서대로 주어진다.
셋째 줄에 주어진 두 연산을 수행해서 구성할 수 있는지 확인할 1에서 n까지 수가 한 번만 나타나는 수열이 순서대로 주어진다.

출력
주어진 두 가지 연산만을 가지고 처음 수열을 결과 수열로 만들 수 있다면 good puzzle, 아니면 bad puzzle을 출력한다.
'''

'''
- 뒤집기를 하든 밀기를 하든 결국 바뀐 수열에서 1부터 시작했을 때 정방향/역방향 둘 중 한방향으로 갔을 때 원래 수열이 나와야 한다.
* Pass/1st/00:11:35
'''
import sys

n = int(sys.stdin.readline())
originalArr = list(map(int, sys.stdin.readline().rstrip().split()))
modifiedArr = list(map(int, sys.stdin.readline().rstrip().split()))

firstIdx = modifiedArr.index(originalArr[0]) # 원래 배열의 첫번째 원소가 있는 위치를 찾음
case1 = modifiedArr[firstIdx:] + modifiedArr[:firstIdx] # 정방향 확인
case2 = modifiedArr[firstIdx + 1:] + modifiedArr[:firstIdx + 1] # 역방향 확인
case2.reverse()

if originalArr == case1 or originalArr == case2:
    print("good puzzle")
else:
    print("bad puzzle")