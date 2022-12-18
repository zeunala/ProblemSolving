'''
최고의 피자

입력
첫째 줄에 토핑의 종류의 수 N(1 ≤ N ≤ 100)이 주어진다.
둘째 줄에는 도우의 가격 A와 토핑의 가격 B가 주어진다. (1 ≤ A, B ≤ 1000)
셋째 줄에는 도우의 열량 C가 주어진다. (1 ≤ C ≤ 10000)
다음 줄부터 N개 줄에는 각 토핑의 열량 Di가 한 줄에 하나씩 주어진다.(1 ≤ Di ≤ 10000)

출력
첫째 줄에 최고의 피자의 1원 당 열량을 출력한다. 소수점 이하는 버리고 정수 값으로 출력한다.
'''

'''
- 각 토핑당 한 번씩만 구매 가능하므로 열량 높은 토핑부터 하나씩 구매하는 식으로 모든 경우의 수를 체크한다.
* Pass/1st/00:06:32
'''
import sys

N = int(sys.stdin.readline().rstrip()) # 토핑 종류의 수
A, B = map(int, sys.stdin.readline().rstrip().split()) # 도우 가격, 토핑 가격
C = int(sys.stdin.readline().rstrip()) # 도우의 열량
arrD = []
for i in range(N):
    arrD.append(int(sys.stdin.readline().rstrip()))
arrD.sort(reverse=True) # 열량 높은 것 우선순위로 정렬

answer = C // A # 1원당 최대 열량(소수점 버림)
currentCal = C # 현재 열량
currentPrice = A # 현재 가격

for e in arrD:
    currentCal += e
    currentPrice += B
    if answer < currentCal // currentPrice:
        answer = currentCal // currentPrice
        
print(answer)