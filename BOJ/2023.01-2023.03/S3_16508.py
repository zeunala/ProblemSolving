'''
전공책

입력
첫 번째 줄에는 민호가 만들고자 하는 단어를 의미하는 문자열 T (1 ≤ |T| ≤ 10)가 주어진다.
T는 항상 대문자이며, |T|는 문자열 T의 길이를 의미한다.
두 번째 줄에는 민호가 가진 전공책의 개수를 의미하는 정수 N (1 ≤ N ≤ 16)이 주어진다.
다음 N개의 각 줄에는 전공책 가격을 의미하는 정수 Ci (10,000 ≤ Ci ≤ 100,000)와 제목을 의미하는 문자열 Wi (1 ≤ |Wi| ≤ 50)가 주어진다.
Wi는 항상 대문자이다.

출력
민호가 원하는 단어 T를 만들기 위해서 선택해야 하는 전공책의 가장 적은 가격의 합을 출력한다. 만약 단어를 만들 수 없다면 -1을 출력한다.
'''

'''
- N의 범위가 작으므로 모든 경우의 수를 탐색하도록 한다.
* Fail/1st/00:11:36
'''
from itertools import product

def isValid(alphaArr, target): # alphaArr로 target 문자를 만들 수 있는지 여부 리턴
    for e in target:
        isExist = False
        for alpha in alphaArr:
            if e in alpha:
                isExist = True
        if isExist == False:
            return False
    return True
    
T = input()
N = int(input())
alphaArr = [set() for _ in range(N)] # alphaArr[i]는 i번째(i>=0) 전공책에 들어있는 알파벳들
priceArr = [0 for _ in range(N)] # priceArr[i]는 i번째 전공책의 가격

for i in range(N):
    a, b  = input().split()
    priceArr[i] = int(a)
    alphaArr[i] = set(b)
    
INF = 10 ** 15
minPrice = INF
for case in product([True, False], repeat = N):
    if isValid([alphaArr[i] for i in range(len(alphaArr)) if case[i]], T):
        price = sum([priceArr[i]  for i in range(len(priceArr)) if case[i]])
        
        if minPrice > price:
            minPrice = price
            
if minPrice == INF:
    print(-1)
else:
    print(minPrice)