'''
돌 게임 3

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 1000)

출력
상근이가 게임을 이기면 SK를, 창영이가 게임을 이기면 CY을 출력한다.
'''

'''
- 기본적으로 N이 1, 3, 4면 선공이 이기고 2면 후공이 이긴다.
N이 5이상일 경우, 1/3/4개를 가져갔을 때 후공이 이기는 N값을 만들 수 있다면 선공이 이긴다.
만약 1/3/4개 어느 경우를 가져가도 선공이 이기는 N값밖에 상대에게 줘야한다면 후공이 이긴다.
* Pass/1st/00:15:01
'''
N = int(input())
maxN = 1000

isFirstWin = [False] * (maxN + 1) # isFirstWin[i]는 N=i일 때 선공이 이기는지 여부
isFirstWin[1] = True
isFirstWin[3] = True
isFirstWin[4] = True

for i in range(5, N + 1):
    # 몇 개를 가져가든 그 다음에 선공이 이기는 수를 넘겨줄 수 밖에 없다면 후공이 이기게 된다.
    if isFirstWin[i - 1] and isFirstWin[i - 3] and isFirstWin[i - 4]:
        isFirstWin[i] = False
    else:
        isFirstWin[i] = True
        
if isFirstWin[N]:
    print("SK")
else:
    print("CY")