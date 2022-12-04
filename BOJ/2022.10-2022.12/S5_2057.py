'''
팩토리얼 분해

입력
첫째 줄에 정수 N이 주어진다.

출력
입력으로 주어진 수를 서로 다른 정수 M개의 팩토리얼의 합으로 나타낼 수 있으면 YES, 없으면 NO를 출력한다. 
'''

'''
- 입력 제한이 20!보다 작다. 따라서 0!~19! 중 모든 경우의 수를 생각해본다. (2 ** 20은 100만정도밖에 되지 않음을 이용)
* Fail/1st/00:09:13/MemoryLimitExceeded
- product 대신 dfs를 이용하도록 수정하였다.
* Pass/2nd/00:14:08
- 문제 풀이 이후 다른 사람의 풀이를 본 결과 그냥 19!부터 0!까지 뺄 수 있는만큼 빼주는 방식으로 구현할 수 있음을 알게 되었다.
'''
from itertools import product

def fact(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

factArr = [fact(i) for i in range(20)] # factArr[i]는 i!의 값 저장
factSum = set() # 19!까지의 가능한 모든 팩토리얼 합들을 저장
def dfs(case):
    if len(case) == 20:
        tempSum = 0
        for i in range(len(case)):
            tempSum += factArr[i] * case[i]
        factSum.add(tempSum)
        return
    
    dfs(case + [0])
    dfs(case + [1])
        
N = int(input())
dfs([])
    
if N != 0 and N in factSum: # 0은 예외로 제거
    print("YES")
else:
    print("NO")
