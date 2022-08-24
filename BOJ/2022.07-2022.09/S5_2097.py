'''
조약돌

입력
첫째 줄에 조약돌의 개수 N(1 ≤ n ≤ 500,000,000)이 주어진다.

출력
첫째 줄에 최소 둘레를 출력한다.
'''

'''
- 최대한 정사각형을 유지하는 식으로 조약돌을 놓는다고 생각한다.
정사각형을 조건으로 했을 때의 한 변의 길이 최솟값을 a라고 하고,
a * a 뿐만 아니라 a * (a - 1)의 직사각형도 가능한지 확인해본다.
* Fail/1st/00:10:12
'''
import math

n = int(input())
width = max(math.ceil(math.sqrt(n)) - 1, 1)
height = width

if (width + 1) * height >= n:
    height -= 1

print(2 * (width + height))