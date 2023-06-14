'''
나머지 계산

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1000)가 주어진다.
둘째 줄부터 T개의 줄에는 진법을 나타내는 B와 음이 아닌 수 B진법 수 D가 공백으로 구분되어 주어진다. (2 ≤ B ≤ 10)
D는 최대 10,000,000자리이다.

출력
각각의 테스트 케이스에 대해서, B진법 수 D를 B-1로 나눈 나머지를 출력한다.
'''

'''
- 10진법으로 변환하고 B-1로 나누되, 자릿수가 매우 클 수 있으므로 일의 자리부터 차례로 변환해가며 B-1로 나눈 나머지를 더해나간다.
* Fail/1st/00:05:22/TimeLimitExceeded
'''
import sys

def solution(B, D): # B진법 문자열 D를 B-1로 나눈 나머지 리턴
    answer = 0
    idx = 1
    
    for i in range(len(D) - 1, -1, -1):
        answer += int(D[i])
        answer %= (B - 1)
        idx * B
        idx %= (B - 1)
    
    return answer

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    B, D = sys.stdin.readline().rstrip().split()
    B = int(B)
    print(solution(B, D))