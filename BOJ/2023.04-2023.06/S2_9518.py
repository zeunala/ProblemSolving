'''
로마 카톨릭 미사

입력
첫째 줄에 R과 S가 주어진다. (1 ≤ R, S ≤ 50)
다음 R개 줄에는 S개의 문자가 주어진다. 이 R × S 개의 문자는 성당에 자리 배치를 나타낸다. '.'은 빈 자리, 'o'는 사람이 앉아있는 자리이다.

출력
평화 의식에서 총 몇 번의 악수가 행해지는지 출력한다.
'''

'''
- 우선 현재 배치를 기준으로 악수를 총 몇 번 이뤄지는지 체크하고,
빈 자리 중 최대 악수가 몇 번까지 가능한지 체크해서 둘을 더하면 된다.
* Pass/1st/00:15:51
'''
import sys

R, S = map(int, sys.stdin.readline().rstrip().split())
arr = []

for i in range(R):
    arr.append(list(sys.stdin.readline().rstrip()))
    
dx = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
answer = 0

for i in range(R):
    for j in range(S):
        if arr[i][j] == ".":
            continue
        
        # 사람이 있는 곳에 대하여 악수가 몇 번 가능한지 체크한다.
        for (di, dj) in dx:
            if i + di >= 0 and i + di < R and j + dj >= 0 and j + dj < S and arr[i + di][j + dj] == "o":
                answer += 1
                
answer //= 2 # 모든 사람에 대하여 체크했으므로 서로 중복해서 체크한 걸 2로 나눠준다.

maxCase = 0 # 최대 가능한 악수 사람 수
for i in range(R):
    for j in range(S):
        if arr[i][j] == "o":
            continue
        
        # 사람이 없는 곳에 대하여 악수가 최대 몇 번 가능한지 체크한다.
        tempCase = 0
        for (di, dj) in dx:
            if i + di >= 0 and i + di < R and j + dj >= 0 and j + dj < S and arr[i + di][j + dj] == "o":
                tempCase += 1
        if tempCase > maxCase:
            maxCase = tempCase
answer += maxCase

print(answer)