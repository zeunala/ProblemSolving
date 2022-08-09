'''
등수 구하기

입력
첫째 줄에 N, 태수의 새로운 점수, 그리고 P가 주어진다.
P는 10보다 크거나 같고, 50보다 작거나 같은 정수, N은 0보다 크거나 같고, P보다 작거나 같은 정수이다.
그리고 모든 점수는 2,000,000,000보다 작거나 같은 자연수 또는 0이다.
둘째 줄에는 현재 랭킹 리스트에 있는 점수가 비오름차순으로 주어진다. 둘째 줄은 N이 0보다 큰 경우에만 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다.
'''

'''
- bisect_right를 이용해서 낮은 점수 순으로 몇 등인지 체크하고, 이를 높은 점수 순위로 바꾸도록 한다.
* Pass/1st/00:10:50
'''
from bisect import bisect_right

N, newScore, P = map(int, input().split())
rankArr = []

if N > 0:
    rankArr = list(map(int, input().split()))

rankArr.sort()
newRank = len(rankArr) + 1 - bisect_right(rankArr, newScore)

if newRank <= P and not (len(rankArr) >= P and rankArr[-P] >= newScore):
    print(newRank)
else:
    print(-1)