'''
신나는 함수 실행

입력
입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다.
입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.

출력
입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.
'''

'''
- 문제의 요구사항을 그대로 구현하되 메모이제이션을 이용해서 이미 계산한 함수 값이 있을 경우 이를 그대로 활용한다.
a, b, c가 1~20일 때만 계산하면 되므로 모든 경우의 수는 20 * 20 * 20 = 8000뿐이다.
* Pass/1st/00:09:30
'''
import sys

sys.setrecursionlimit(10000)
funcValue = {} # 이미 계산한 함수 값들 저장

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if (a, b, c) in funcValue:
        return funcValue[(a, b, c)]
    
    result = 0
    if a < b and b < c:
        result = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        result = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    funcValue[(a, b, c)] = result
    return result

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w({0}, {1}, {2}) = {3}".format(a, b, c, w(a, b, c)))