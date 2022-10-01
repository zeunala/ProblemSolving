'''
동전 뒤집기

입력
첫째 줄에 20이하의 자연수 N이 주어진다.
둘째 줄부터 N줄에 걸쳐 N개씩 동전들의 초기 상태가 주어진다.
각 줄에는 한 행에 놓인 N개의 동전의 상태가 왼쪽부터 차례대로 주어지는데,
앞면이 위를 향하도록 놓인 경우 H, 뒷면이 위를 향하도록 놓인 경우 T로 표시되며 이들 사이에 공백은 없다.

출력
첫째 줄에 한 행 또는 한 열에 놓인 N개의 동전을 모두 뒤집는 작업들을 수행하여 뒷면이 위를 향하여 놓일 수 있는 동전의 최소 개수를 출력한다.
'''

'''
- 2^20은 약 100만이므로 우선 브루트 포스를 이용해보고 시간초과가 나지 않도록 최적화를 해본다.
* Pass/1st/00:21:14(use PyPy3)
- 이후 다른 풀이를 참조한 결과 비트마스킹을 사용하여 좀 더 최적화시킬 수 있을 것이라 생각한다.
'''
from itertools import product

N = int(input())
arr = [[] for _ in range(N)] # 앞면: -1, 뒷면: 1
allCase = list(product([-1, 1], repeat = N)) # 각 열을 뒤집는 모든 경우의 수, 이 후 각 케이스들에 대하여 행을 뒤집을 것임.
answer = 10 ** 10 # 현재까지의 최소 뒷면의 개수

for i in range(N):
    tempArr = list(input())
    for j in range(len(tempArr)):
        if tempArr[j] == "H":
            arr[i].append(-1)
        else: # tempArr[i] == "T"
            arr[i].append(1)
            
for case in allCase:
    tempAnswer = 0
    
    for i in range(N): # 각 케이스에 대하여 각 행들을 확인
        currentLine = 0 # 현재 라인의 뒷면 수
        
        # 행을 뒤집기 전의 그 행의 뒷면 수 확인
        for j in range(N):
            currentLine += max(case[j] * arr[i][j], 0)
        # 뒷면 수가 많다면 그 행을 뒤집고, 그렇지 않다면 그대로 둔다
        currentLine = min(currentLine, N - currentLine)
        
        tempAnswer += currentLine
        
        
        if tempAnswer > answer: # 조기차단
            break
        
    if tempAnswer < answer:
        answer = tempAnswer
        
print(answer)