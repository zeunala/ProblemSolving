'''
숫자 정사각형

첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에 수가 주어진다.

출력
첫째 줄에 정답 정사각형의 크기를 출력한다.
'''

'''
- 숫자의 범위가 크지 않으므로 최대크기의 정사각형일 때부터 모든 경우의 수를 찾아보도록 한다.
* Pass/1st/00:07:54
'''
N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(input()))

answer = 1
for x in range(min(N, M), 1, -1):
    for i in range(N - x + 1):
        for j in range(M - x + 1):
            if arr[i][j] == arr[i+x-1][j] == arr[i][j+x-1] == arr[i+x-1][j+x-1]:
                answer = x ** 2
    
    if answer > 1:
        break

print(answer)