'''
보석 상자

입력
첫째 줄에 아이들의 수 N과 색상의 수 M이 주어진다. (1 ≤ N ≤ 10^9, 1 ≤ M ≤ 300,000, M ≤ N)
다음 M개 줄에는 구간 [1, 10^9]에 포함되는 양의 정수가 하나씩 주어진다.
K번째 줄에 주어지는 숫자는 K번 색상 보석의 개수이다.

출력
첫째 줄에 질투심의 최솟값을 출력한다.
'''

'''
- 아이들의 수와 각 색상들, 질투심의 수 H가 주어졌을 때 나눠줄 수 있는 방법이 있는지 체크하는 함수를 만든다.
이때 아이들의 수와 각 색상들이 고정되어 있다면 H는 연속적이므로 파라매트릭 서치로 접근할 수 있다.
* Pass/1st/00:13:52
'''
import sys

def isValidWay(N, arrM, H): # 최대 질투심의 수가 H미만이 되도록 분배할 수 있는지 여부 리턴
    if H == 0:
        return sum(arrM) == 0
    
    needN = 0
    for e in arrM:
        needN += e // H + min(e % H, 1) # 예를 들어 색상이 A인 보석이 7이고, 최대 질투심의 수가 3이면 최대 3명이 필요하다.
    return needN <= N

N, M = map(int, sys.stdin.readline().rstrip().split()) # N: 아이들의 수, M: 색상의 수
arrM = [] # 각 색상별 개수
for i in range(M):
    arrM.append(int(sys.stdin.readline().rstrip()))
    
minH = 0
maxH = sum(arrM)
answerH = maxH

while minH <= maxH:
    midH = (minH + maxH) // 2
    
    if isValidWay(N, arrM, midH):
        if answerH > midH:
            answerH = midH
        maxH = midH - 1
    else:
        minH = midH + 1
        
print(answerH)
    