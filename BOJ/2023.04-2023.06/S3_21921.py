'''
블로그

입력
첫째 줄에 블로그를 시작하고 지난 일수 N와 X가 공백으로 구분되어 주어진다.
둘째 줄에는 블로그 시작 1일차부터 N일차까지 하루 방문자 수가 공백으로 구분되어 주어진다.

출력
첫째 줄에 X일 동안 가장 많이 들어온 방문자 수를 출력한다. 만약 최대 방문자 수가 0명이라면 SAD를 출력한다.
만약 최대 방문자 수가 0명이 아닌 경우 둘째 줄에 기간이 몇 개 있는지 출력한다.
'''

'''
- 문제의 요구사항을 그대로 구현하면 된다.
* Pass/1st/00:22:31
'''
import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

maxVisited = 0
maxCount = 0
currentVisited = 0

# 처음 X일 기준
for i in range(X):
    currentVisited += arr[i]
maxVisited = currentVisited
maxCount = 1

for i in range(X, N):
    currentVisited += arr[i] # 새로운 방문자
    currentVisited -= arr[i - X] # 빠지는 방문자

    if maxVisited < currentVisited:
        maxVisited = currentVisited
        maxCount = 1
    elif maxVisited == currentVisited:
        maxCount += 1

if maxVisited == 0:
    print("SAD")
else:
    print(maxVisited)
    print(maxCount)