'''
집합

입력
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

출력
check 연산이 주어질때마다, 결과를 출력한다.
'''

'''
- 파이썬의 집합 자료형을 이용해 하나하나 구현해본다.
* Pass/1st/00:08:09
- PyPy3으로 채점하면 메모리초과가 발생하는데 다른 사람의 의견을 본 결과 비트마스킹을 이용해서 최적화할 수 있을 것으로 보인다.
'''
import sys

M = int(sys.stdin.readline().rstrip())
S = set()

for i in range(M):
    nextLine = list(sys.stdin.readline().rstrip().split())
    if len(nextLine) == 2:
        nextLine[1] = int(nextLine[1])
    
    if nextLine[0] == "add":
        S.add(nextLine[1])
    elif nextLine[0] == "remove":
        if nextLine[1] in S:
            S.remove(nextLine[1])
    elif nextLine[0] == "check":
        if nextLine[1] in S:
            print(1)
        else:
            print(0)
    elif nextLine[0] == "toggle":
        if nextLine[1] in S:
            S.remove(nextLine[1])
        else:
            S.add(nextLine[1])
    elif nextLine[0] == "all":
        S = set(range(1, 21))
    elif nextLine[0] == "empty":
        S = set()