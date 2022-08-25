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
- 가로/세로 길이가 최소 1이어야 하므로, height가 0이 되지 않도록 해야한다.
* Pass/2nd/00:12:17
'''
import math

n = int(input())
width = max(math.ceil(math.sqrt(n)) - 1, 1)
height = width

if (width + 1) * height >= n:
    height -= 1

if height == 0:
    height = 1

print(2 * (width + height))