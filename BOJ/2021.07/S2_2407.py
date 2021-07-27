'''
조합

입력
n과 m이 주어진다. (5 ≤ n ≤ 100, 5 ≤ m ≤ 100, m ≤ n)

출력
nCm을 출력한다.
'''

'''
- 그냥 파이썬의 from itertools import combinations 이용하는게 제일 편할 것 같지만 그래도 수학적으로 구해보자
nCm=nPm/m!=n!/(n-m)!m!을 이용해보자.
* Pass/1st/00:04:26
'''
def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n, m = map(int, input().split())
print(fact(n)//(fact(n-m)*fact(m)))