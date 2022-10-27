'''
설탕 배달

입력
첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

출력
상근이가 배달하는 봉지의 최소 개수를 출력한다.
만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
'''

'''
- N의 범위가 크지 않으므로 1킬로그램부터 하나씩 최소 봉지수를 체크해나간다.
* Pass/1st/00:08:24
'''
N = int(input())
INF = 10 ** 10

arr = [INF] * max(5 + 1, N + 1)
arr[3] = 1
arr[5] = 1

for i in range(6, N + 1):
    arr[i] = min(min(arr[i - 3], arr[i - 5]) + 1, INF)

if arr[N] == INF:
    print(-1)
else:
    print(arr[N])