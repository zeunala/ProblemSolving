'''
경매

입력
첫째 줄에 두 정수 U(1 ≤ U ≤ 10,000), N(1 ≤ N ≤ 100,000)이 주어진다.
U는 금액의 상한이고, N은 경매에 참여한 회수이다.
다음 N개의 줄에는 사람 이름 S(공백 없는 알파벳 대소문자 10자 이하)와,
그 사람이 제시한 가격 P(1 ≤ P ≤ U, 정수)이 경매에 참여한(가격을 제시한) 순서대로 주어진다.

출력
첫째 줄에 낙찰된 사람의 이름과 그 가격을 출력한다.
'''

'''
- 가장 적은 수가 제시한 가격 -> 그 중 최저가 -> 그 중 가장 먼저 입찰할 사람 순으로 찾는다.
* Pass/1st/00:09:55
'''
import sys
from collections import defaultdict

U, N = map(int, sys.stdin.readline().rstrip().split())
priceArr = defaultdict(int) # priceArr[i]는 i원을 몇 명이 입찰했는지
peopleArr = [[] for _ in range(U + 1)] # peopleArr[i]는 i원을 누가 입찰했는지

# 입력 받음
for i in range(N):
    name, price = sys.stdin.readline().rstrip().split()
    priceArr[int(price)] += 1
    peopleArr[int(price)].append(name)
    
# 가장 적은 수가 제시한 가격을 찾음
minPeople = min(priceArr.values())

# 그 중 최저가를 찾음
minPrice = min([i for i in range(U + 1) if priceArr[i] == minPeople])

print(peopleArr[minPrice][0], minPrice)
