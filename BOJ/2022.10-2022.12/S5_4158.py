'''
CD

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스의 첫째 줄에는 상근이가 가지고 있는 CD의 수 N, 선영이가 가지고 있는 CD의 수 M이 주어진다.
N과 M은 최대 백만이다. 다음 줄부터 N개 줄에는 상근이가 가지고 있는 CD의 번호가 오름차순으로 주어진다.
다음 M개 줄에는 선영이가 가지고 있는 CD의 번호가 오름차순으로 주어진다.
CD의 번호는 십억을 넘지 않는 양의 정수이다. 입력의 마지막 줄에는 0 0이 주어진다.
상근이와 선영이가 같은 CD를 여러장 가지고 있는 경우는 없다.

출력
두 사람이 동시에 가지고 있는 CD의 개수를 출력한다.
'''

'''
- 집합 자료형을 이용하면 쉽겠으나 시간 초과의 위험이 있을 것으로 보인다.
입력이 오름차순으로 주어지므로 포인터를 하나씩 두어 움직이는 방식으로 진행한다.
* Fail/1st/00:05:47
'''
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arrN = []
arrM = []

for i in range(N):
    arrN.append(int(sys.stdin.readline().rstrip()))
for i in range(M):
    arrM.append(int(sys.stdin.readline().rstrip()))
sys.stdin.readline() # 마지막 0 0
    
idxN = 0
idxM = 0
answer = 0

while idxN < len(arrN) and idxM < len(arrM):
    if arrN[idxN] == arrM[idxM]:
        idxN += 1
        idxM += 1
        answer += 1
    elif arrN[idxN] > arrM[idxM]:
        idxM += 1
    elif arrN[idxN] < arrM[idxM]:
        idxN += 1
        
print(answer)