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
- 잘못 작성한 코드를 수정하였다.
* Pass/2nd/00:31:26(use PyPy3)
- 기존 코드에서도 테스트 코드가 맞은 이유가 궁금했는데, 다른 사람의 풀이를 보니
B진법의 수 abcd는 (B ** 3) a + (B ** 2) b + (B ** 1) c + d이고, (B ** n) * a를 B-1로 나눈 나머지는
a mod (B - 1) * ((B mod (B - 1)) ** n) = a mod (B - 1) * (1 mod (B - 1) ** n) = a mod (B - 1),
즉 자릿수와 상관없이 나머지가 나오고 따라서 그냥 모든 숫자들을 더해주고 B - 1로 나눠줘도 동일한 결과가 나옴을 알게 되었다.
또한 성능상 첫 번째 코드와 두 번째 코드가 별 차이가 없었고 첫 번째 제출한 코드 역시 PyPy3로 채점하니 정답이 나왔다.
'''
import sys

def solution(B, D): # B진법 문자열 D를 B-1로 나눈 나머지 리턴
    answer = 0
    for i in range(len(D) - 1, -1, -1):
        answer *= B
        answer += int(D[i])
        answer %= (B - 1)
    
    return answer

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    B, D = sys.stdin.readline().rstrip().split()
    B = int(B)
    print(solution(B, D))