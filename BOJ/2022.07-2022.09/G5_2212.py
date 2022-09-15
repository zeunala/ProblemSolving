'''
센서

입력
첫째 줄에 센서의 개수 N(1 ≤ N ≤ 10,000), 둘째 줄에 집중국의 개수 K(1 ≤ K ≤ 1000)가 주어진다.
셋째 줄에는 N개의 센서의 좌표가 한 개의 정수로 N개 주어진다.
각 좌표 사이에는 빈 칸이 하나 있으며, 좌표의 절댓값은 1,000,000 이하이다.

출력
첫째 줄에 문제에서 설명한 최대 K개의 집중국의 수신 가능 영역의 길이의 합의 최솟값을 출력한다.
'''

'''
- 우선 센서 좌표들을 오름차순으로 배열하자.
센서 좌표가 a~b 범위에 있을 때 이를 잇는 긴 선에서 K-1개의 구간을 지우되 최대한 많이 지운다고 생각하면 될 것으로 보인다.
* Pass/1st/00:10:15
'''
import sys

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()
answer = arr[-1] - arr[0] # 여기서 N-1개의 구간을 지운다.

arrGap = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)] # 센서의 구간 차이들을 적어놓았다가, 여기서 큰 것부터 지워나간다.
arrGap.sort()

for i in range(K - 1):
    if arrGap:
        answer -= arrGap.pop()

print(answer)