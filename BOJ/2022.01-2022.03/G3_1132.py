'''
입력
첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에는 각 수가 주어진다. 수의 길이는 최대 12이다.
적어도 한 알파벳은 수의 가장 처음에 주어지지 않는다.

출력
첫째 줄에 합의 최댓값을 출력한다.
'''

'''
- 총 합에서 A~J가 몇 번 곱해지는지 계산해서 그 수가 적은 것부터 작은 수를 할당한다.
다만 맨 앞에 나왔던 적이 있는 알파벳은 0이 될 수 없음에 주의한다.
* Pass/1st/00:16:58
'''
import heapq

N = int(input())
arr = []
for i in range(N):
    arr.append(input())
    
alpha = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0,
         'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0} # 각 알파벳이 몇 번씩 곱해지는지를 나타냄
matchAlpha = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0,
              'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0} # 알파벳이 어느 숫자와 매핑되는지를 나타냄
notZero = [] # 0이 될 수 없는 알파벳들

for e in arr:
    idx = 1
    for i in range(len(e) - 1, -1, -1): # 끝에서부터 계산
        alpha[e[i]] += idx
        idx *= 10
        
for e in arr:
    if e[0] not in notZero:
        notZero.append(e[0])
        
minHeap = [] # (개수, 알파벳)이 와서 개수가 작은 것부터 앞에 오도록 함
for e in alpha.keys():
    heapq.heappush(minHeap, (alpha[e], e))

remainNum = [True for _ in range(10)] # remainNum[i]는 숫자 i가 될 수 있는 자리가 남아있는지 여부를 나타냄    
    

while minHeap:
    a, b = heapq.heappop(minHeap) # a: 개수, b: 알파벳
    for i in range(10):
        if not remainNum[i]: # 자리가 없으면 다음 숫자 탐색
            continue
        if i == 0 and b in notZero: # 0 차례인데 b가 0이 될 수 없어서도 안 됨
            continue
        matchAlpha[b] = i
        remainNum[i] = False
        break

answer = 0
for e in "ABCDEFGHIJ":
    answer += alpha[e] * matchAlpha[e]
print(answer)