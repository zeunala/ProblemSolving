'''
로프

입력
첫째 줄에 정수 N이 주어진다.
다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다.
이 값은 10,000을 넘지 않는 자연수이다.

출력
첫째 줄에 답을 출력한다.
'''

'''
- 로프가 a개 있고 가장 약한 로프가 중량 b까지 들 수 있다면 들 수 있는 최대는 a*b임을 이용한다.
* Pass/1st/00:05:02
'''
import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()

answer = 0
for i in range(N):
    temp = arr[i] * (N - i) # i번째로(i>=0) 가벼운 로프부터 모두 이용했을 때 들 수 있는 최대 중량
    if temp > answer:
        answer = temp
        
print(answer)