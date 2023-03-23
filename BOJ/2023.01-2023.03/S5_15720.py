'''
카우버거

입력
첫째 줄에는 주문한 버거의 개수 B, 사이드 메뉴의 개수 C, 음료의 개수 D가 공백을 사이에 두고 순서대로 주어진다. (1 ≤ B, C, D ≤ 1,000)
둘째 줄에는 각 버거의 가격이 공백을 사이에 두고 주어진다.
셋째 줄에는 각 사이드 메뉴의 가격이 공백을 사이에 두고 주어진다.
넷째 줄에는 각 음료의 가격이 공백을 사이에 두고 주어진다.
각 메뉴의 가격은 100의 배수이며, 10000원을 넘지 않는다.

출력
첫째 줄에는 세트 할인이 적용되기 전 가격을 출력한다.
둘째 줄에는 세트 할인이 적용된 후의 최소 가격을 출력한다.
'''

'''
- 세트를 최대한 비싼 물품을 우선순위로 구현하면 되는 그리디 알고리즘이다.
각 버거/사이드/음료를 가격 순으로 정렬하고 비싼 것부터 세트로 짝짓도록 한다.
* Pass/1st/00:06:45
'''
import sys

B, C, D = map(int, sys.stdin.readline().rstrip().split())
# 비싼 것부터 정렬
arrB = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)
arrC = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)
arrD = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)

# 할인 전 가격
beforePrice = sum(arrB) + sum(arrC) + sum(arrD)

# 할인 후 가격
setCount = min(len(arrB), len(arrC), len(arrD)) # 버거/사이드/음료 중 가장 개수가 적은 것만큼 세트를 구성할 수 있다.
afterPrice = beforePrice - (sum(arrB[:setCount]) + sum(arrC[:setCount]) + sum(arrD[:setCount])) // 10 # 세트 구성시 10퍼센트 할인

print(beforePrice)
print(afterPrice)