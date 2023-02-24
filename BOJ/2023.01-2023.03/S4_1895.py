'''
필터

입력
첫째 줄에 이미지의 크기 R과 C가 주어진다.
그 다음 R개의 각 줄에는 C개의 픽셀 값이 주어진다.
마지막 줄에는 T값이 주어진다.

출력
첫째 줄에 필터링 된 이미지 J의 각 픽셀 값 중에서 T보다 크거나 같은 것의 개수를 출력한다.
'''

'''
- R, C의 범위가 크지 않으므로 문제 요구사항을 그대로 구현하면 된다.
* Pass/1st/00:06:09
'''
import sys

R, C = map(int, sys.stdin.readline().rstrip().split())
arr = []

for i in range(R):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
T = int(sys.stdin.readline().rstrip())
answer = 0

for i in range(R - 2):
    for j in range(C - 2):
        if sorted([arr[i][j], arr[i][j + 1], arr[i][j + 2],
                   arr[i + 1][j], arr[i + 1][j + 1], arr[i + 1][j + 2],
                   arr[i + 2][j], arr[i + 2][j + 1], arr[i + 2][j + 2]])[4] >= T:
            answer += 1
            
print(answer)