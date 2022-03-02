'''
다각형의 면적

입력
첫째 줄에 N이 주어진다.
다음 N개의 줄에는 다각형을 이루는 순서대로 N개의 점의 x, y좌표가 주어진다.
좌표값은 절댓값이 100,000을 넘지 않는 정수이다.

출력
첫째 줄에 면적을 출력한다.
면적을 출력할 때에는 소수점 아래 둘째 자리에서 반올림하여 첫째 자리까지 출력한다.
'''

'''
- 고등학교 때 배웠던 면적 공식을 이용한다.
* Pass/1st/00:07:06
'''
import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr.append((a, b))
    
arr.append(arr[0])

SumA = 0
SumB = 0
for i in range(N):
    SumA += arr[i][0] * arr[i+1][1]
    SumB += arr[i+1][0] * arr[i][1]

SumAll = round(0.5 * abs(SumA - SumB), 1)
print(SumAll)

