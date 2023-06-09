'''
0 만들기

입력
첫 번째 줄에 테스트 케이스의 개수가 주어진다(<10).
각 테스트 케이스엔 자연수 N이 주어진다(3 <= N <= 9).

출력
각 테스트 케이스에 대해 ASCII 순서에 따라 결과가 0이 되는 모든 수식을 출력한다. 각 테스트 케이스의 결과는 한 줄을 띄워 구분한다.
'''

'''
- N의 범위가 작으므로 +, -, 공백 중에서 가능한 모든 경우의 수를 탐색한다. (최대 3^8가지)
* Fail/1st/00:08:57
'''
from itertools import product

def getResult(N, case): # 1+2-3과 같은 수식을 얻어 리턴
    result = ""
    for j in range(N - 1):
        result += str(j + 1) + case[j]
    result += str(N)
    return result

def isValid(N, case):
    return eval(getResult(N, case).replace(" ", "")) == 0
    

T = int(input())
for i in range(T):
    N = int(input())
    
    for case in product("+- ", repeat=N-1):
        if isValid(N, case):
            print(getResult(N, case))
    print()