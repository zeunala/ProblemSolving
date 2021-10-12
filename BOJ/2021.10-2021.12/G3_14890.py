'''
경사로

입력
첫째 줄에 N (2 ≤ N ≤ 100)과 L (1 ≤ L ≤ N)이 주어진다. 둘째 줄부터 N개의 줄에 지도가 주어진다. 각 칸의 높이는 10보다 작거나 같은 자연수이다.

출력
첫째 줄에 지나갈 수 있는 길의 개수를 출력한다.
'''

'''
- 문제의 조건을 보아 가로 세로 각각 따로 경사로를 놓을 수 있는 것으로 보이므로, 2N개의 길에 대한 배열을 우선 만든다.
각 길에 대해서 쭉 직진해가다가, 1차이 나는 곳을 만나면 거기에 경사로를 놓는다고 가정, (1이상 차이나면 횡단 불가)
만약 경사로를 다 놓기전에 높이가 변하면 횡단 불가로 처리한다.
* Pass/1st/00:52:30
- 경사로 놓였는지 기존 길/이후 길을 중복해서 확인하지 않도록 combo변수를 사용하였었는데,
풀이 이후 다른 답안을 보니 그렇게 하지 않아도 시간초과가 나지는 않는 것 같다.
경사로가 연속해서 배치하는 등의 상황에서 combo가 다소 비직관적이기 때문에 길을 재확인하는 방법이 더 나은 풀이일 것으로 보인다.
'''
import sys

def checkStreet(street, L): # 길 한줄의 배열과 L값을 입력받아 횡단가능여부를 True/False로 리턴
    N = len(street)
    #stairExist = [False for _ in range(N)] # 그 자리에 경사로가 놓였는지 유무

    nowHeight = street[0] # 지금 서있는 높이
    nextWalk = 1 # 다음 밟아야 하는 길 번호
    combo = 1 # nowHeight가 몇번까지 유지되었는지 카운트(만약 0이하이면 경사로를 밟고 있는 중이며 1-combo만큼 더 가야함을 뜻한다)

    while nextWalk < N:
        if street[nextWalk] == nowHeight:
            nextWalk += 1
            combo += 1
        elif street[nextWalk] == nowHeight + 1: # 다음 밟을 곳이 현재보다 한 칸 높음(현재까지 밟은 곳들에다 경사로를 세워야함)
            if combo < L: # 현재길 포함 총 L개의 높이가 같지 않으므로 경사로를 세울 수 없음
                return False
            else:
                nowHeight = street[nextWalk]
                nextWalk += 1
                combo = 1 # combo가 다시 시작됨
        elif street[nextWalk] == nowHeight - 1: # 다음 밟을 곳이 현재보다 한 칸 낮음(앞으로 밟을 곳에다 경사로를 세워야함)
            if combo < 0: # 아직 경사로를 밟고 있다면 경사로를 세울 수 없음(combo가 0일 때도 가능한 건 내리막길 연속이 가능하기 때문)
                return False
            elif nextWalk + (L-1) >= N: # 경사로가 길의 끝을 넘길 수도 없음
                return False
            else:
                nowHeight = street[nextWalk]
                nextWalk += 1
                combo = 1 - L # L만큼 경사로를 걸어야 1부터 다시 카운트 됨
        else:
            return False
    
    return True

N, L = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in range(N):
    tempArr = []
    for j in range(N):
        tempArr.append(arr[j][i])
    arr.append(tempArr) # 입력기준 세로 방향으로 arr에 하나 더 추가한다.

answer = 0
for e in arr:
    if checkStreet(e, L):
        answer += 1
print(answer)