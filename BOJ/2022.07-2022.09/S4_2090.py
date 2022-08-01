'''
조화평균

입력
첫째 줄에 자연수 N(1≤N≤9)이 주어진다.
다음 줄에는 차례로 A[1], …, A[N]이 주어진다.
각 수들은 자연수이며, 100을 넘지 않는다.

출력
첫째 줄에 분수 형태로 답을 출력한다.
답을 표현하는 방법이 여러 가지 있을 수 있는데,
그 중에서 가장 적은 수의 문자(숫자 및 /)를 사용하는 답을 출력하고,
그러한 경우가 여럿 있다면 사전 식으로 제일 앞서는 것을 출력한다.
'''

'''
- 문제의 조건에 따라 조화평균을 구하고 약분하도록 한다.
조화평균의 분자는 모든 수들의 곱이고, 분모는 (모든 수들의 곱 / 각각의 수들)의 합이 된다.
* Pass/1st/00:06:59
- 다른 사람의 의견을 본 결과 fractions.Fraction을 이용하면 쉽게 계산할 수 있음을 알게 되었다.
'''
import math

N = int(input())
arr = list(map(int, input().split()))

arrCrossValue = 1 # 모든 수들의 곱
for e in arr:
    arrCrossValue *= e
    
upNum = arrCrossValue # 분자
downNum = 0 # 분모
for e in arr:
    downNum += (arrCrossValue // e)
    
# 약분
upDownGcd = math.gcd(upNum, downNum)
upNum //= upDownGcd
downNum //= upDownGcd

print(str(upNum) + "/" + str(downNum))