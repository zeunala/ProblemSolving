'''
관중석

입력
첫 줄에 원의 반지름 D1과 D2가 양의 정수로 주어진다. 단, 1 ≤ D1 ≤ D2 ≤ 2,000이다.

출력
사용되는 좌석의 수를 나타내는 하나의 양의 정수를 출력한다. 
'''

'''
- 좌석을 0이상 1미만의 기약분수로 나타내고, 서로 다른 여러 개의 좌석의 개수를 세면 된다.
예를 들어 D가 3일 때는 0/3, 1/3, 2/3으로 나타낼 수 있으며,
D가 6일 때는 0/6, 1/6, 2/6, 3/6, 4/6, 5/6으로 나타낼 수 있다.
서로 다른 분수의 개수를 모두 세면 된다. 즉 1/3과 2/6같은 중복은 하나만 센다.
* Fail/1st/00:09:52
'''
import math

def getDivTuple(a, b): # a/b의 분수를 약분해서 (a, b)의 형태로 반환
    gcdAB = math.gcd(a, b)
    return (a // gcdAB, b // gcdAB)

D1, D2 = map(int, input().split())
totalCase = set()

for i in range(D1, D2 + 1):
    for j in range(i):
        totalCase.add(getDivTuple(j, i))
        
print(len(totalCase))