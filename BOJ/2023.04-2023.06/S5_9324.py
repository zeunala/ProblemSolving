'''
진짜 메시지

입력
첫째 줄에 100 이하의 테스트 케이스의 개수가 주어진다. 그리고 각 테스트 케이스마다
대문자로만 이루어진 10만자 이하의 문자열 M이 한 줄에 주어진다. 이 문자열은 검사해야할 메시지다.

출력
테스트 케이스마다 메시지 M이 진짜 메시지면 “OK”를, 가짜 메시지면 “FAKE”를 한 줄에 출력한다.
'''

'''
- 메시지를 처음부터 스캔하면서, 특정 문자가 3의 배수가 될 경우 바로 다음에 그 문자가 중복해서 오는지 확인한다. (그 문제는 개수에 포함X)
만약 그렇지 않다면 가짜 메시지로 판단하고, 끝까지 스캔해도 이상이 없으면 진짜 메시지로 판단한다.
* Pass/1st/00:07:09
'''
from collections import defaultdict
import sys

def isValidMessage(M):
    idx = 0
    alphaDict = defaultdict(int) # 각 문자별로 몇 번 등장했는지
    
    while idx < len(M):
        alphaDict[M[idx]] += 1
        
        if alphaDict[M[idx]] % 3 == 0: # 같은 문자가 3의 배수개 등장할 경우
            if idx + 1 >= len(M) or M[idx + 1] != M[idx]: # 그 문자가 연달아 등장해야 한다.
                return False
            idx += 1 # 중복해서 와야하는 문자는 alphaDict에 기록하지 않은 상태로 넘김
        idx += 1
    return True
        
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    M = sys.stdin.readline().rstrip()
    
    if isValidMessage(M):
        print("OK")
    else:
        print("FAKE")