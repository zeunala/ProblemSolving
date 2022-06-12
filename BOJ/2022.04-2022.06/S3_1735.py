'''
분수 합

입력
첫째 줄과 둘째 줄에, 각 분수의 분자와 분모를 뜻하는 두 개의 자연수가 순서대로 주어진다.
입력되는 네 자연수는 모두 30,000 이하이다.

출력
첫째 줄에 구하고자 하는 기약분수의 분자와 분모를 뜻하는 두 개의 자연수를 빈 칸을 사이에 두고 순서대로 출력한다.
'''

'''
- 분모의 최소공배수를 구해서 두 분수를 합친 뒤, 분모와 분자의 최대공약수로 나눠주면 될 것으로 보인다.
* Pass/1st/00:06:19
'''
import math

# A, B는 첫 번째 분수의 분자, 분모
A, B = map(int, input().split())
# C, D는 두 번째 분수의 분자, 분모
C, D = map(int, input().split())

# 분수 합의 분모
F = (B * D) // math.gcd(B, D)
# 분수 합의 분자
E = A * (F // B) + C * (F // D)

# 기약분수로 만듦
gcdEF = math.gcd(E, F)
E //= gcdEF
F //= gcdEF

print(str(E), str(F))