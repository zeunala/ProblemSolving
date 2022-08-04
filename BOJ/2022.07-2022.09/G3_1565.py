'''
수학

입력
첫째 줄에 D의 크기와 M의 크기가 주어진다.
둘째 줄에 배열 D, 셋째 줄에 배열 M이 주어진다.
D와 M의 크기는 50보다 작거나 같고, 그 속에 들어있는 수는 모두 10^9보다 작거나 같은 양의 정수이다.

출력
첫째 줄에 개수를 출력한다.
'''

'''
- 셋째 줄의 최대공약수 / 둘째 줄의 최소공배수 의 약수의 개수를 계산한다.
* Fail/1st/00:18:08/TimeOver
- 시간을 좀 더 짧게 하도록 최적화하였다.
* Fail/2nd/00:23:30/TimeOver
- 큰 수 소수 입력을 대비해 checkDiv 함수를 수정하였다.
* Pass/3rd/00:35:10
'''
import math
from collections import defaultdict

def checkDiv(n, start): # 1이 아닌 n의 약수 중 최솟값 리턴
    for i in range(start, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n

D, M = map(int, input().split())
arrD = list(map(int, input().split()))
arrM = list(map(int, input().split()))
gcdArrM = math.gcd(*arrM)
lcmArrD = math.lcm(*arrD)
target = gcdArrM // lcmArrD

if gcdArrM % lcmArrD != 0:
    print(0)
elif target == 1:
    print(1)
else:
    temp = defaultdict(int) # 소인수들의 모임
    targetDiv = 2
    while target > 1:
        targetDiv = checkDiv(target, targetDiv)
        target //= targetDiv
        temp[targetDiv] += 1
        
    result = 1
    for e in temp.keys():
        result *= (temp[e] + 1)
    print(result)