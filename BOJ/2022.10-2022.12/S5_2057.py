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
'''
from itertools import product

def fact(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

N = int(input())
factArr = [fact(i) for i in range(20)] # factArr[i]는 i!의 값 저장
allCase = list(product((0, 1), repeat = len(factArr)))

factSum = set() # 19!까지의 가능한 모든 팩토리얼 합들을 저장
for case in allCase:
    tempSum = 0
    for i in range(len(case)):
        tempSum += factArr[i] * case[i]
    factSum.add(tempSum)
    
if N != 0 and N in factSum: # 0은 예외로 제거
    print("YES")
else:
    print("NO")
