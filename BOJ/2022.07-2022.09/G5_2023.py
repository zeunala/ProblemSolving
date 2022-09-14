'''
신기한 소수

입력
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다.

출력
N자리 수 중에서 신기한 소수를 오름차순으로 정렬해서 한 줄에 하나씩 출력한다.
'''

'''
- 한 자리 소수 2, 3, 5, 7 기준으로 bfs로 N자리가 될 때까지 하나하나 찾도록 한다.
* Fail/1st/00:12:47
'''
from collections import deque
import math

def checkPrime(n): # n이 소수인지 유무를 리턴
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True
    
N = int(input())
answer = deque([2, 3, 5, 7]) # 여기서 왼쪽부터 하나씩 떼어서 소수인 경우를 뒤에 붙일 것임
while answer[0] < (10 ** (N - 1)): # (N-1)자리를 다 떼어낼 때까지 반복
    temp = answer.popleft()
    for i in range(1, 10, 2): # 뒤에 짝수를 붙이면 무조건 소수가 아니므로 홀수를 붙이는 경우만 생각한다.
        if checkPrime(temp * 10 + i):
            answer.append(temp * 10 + i)

while answer:
    print(answer.popleft())