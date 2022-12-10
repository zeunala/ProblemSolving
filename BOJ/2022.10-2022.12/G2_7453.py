'''
합이 0인 네 정수

입력
첫째 줄에 배열의 크기 n (1 ≤ n ≤ 4000)이 주어진다.
다음 n개 줄에는 A, B, C, D에 포함되는 정수가 공백으로 구분되어져서 주어진다.
배열에 들어있는 정수의 절댓값은 최대 2^28이다.

출력
합이 0이 되는 쌍의 개수를 출력한다.
'''

'''
- A, B에서 얻을 수 있는 합과 C, D에서 얻을 수 있는 합 두 부분으로 나눈다.
전자의 합에 대해 합이 0이 되도록 하는 후자의 합이 몇 개 인지를 기록해두도록 한다.
* Fail/1st/00:09:05/TimeLimitExceeded
- 오류를 수정하고 더 빠르게 계산할 방법을 고민해본다.
* Fail/2nd/00:23:21/TimeLimitExceeded
- defaultdict 대신 일반 딕셔너리를 이용하는 방법을 사용해본다.
* Fail/3rd/00:33:28/RuntimeError
- 오류를 수정하고 연산을 중복하지 않도록 수정하였다.
* Fail/4th/00:34:29/TimeLimitExceeded
'''
import sys

N = int(sys.stdin.readline().rstrip())
A = []
B = []
C = []
D = []
dictAB = {} # key는 A와 B의 합, value는 그것의 개수
dictCD = {} # key는 C와 D의 합, value는 그것의 개수
answer = 0

for i in range(N):
    t1, t2, t3, t4 = map(int, sys.stdin.readline().rstrip().split())
    A.append(t1)
    B.append(t2)
    C.append(t3)
    D.append(t4)
    
# 가능한 합의 경우들을 저장
for i in range(N):
    for j in range(N):
        sumAB = A[i] + B[j]
        if sumAB in dictAB:
            dictAB[sumAB] += 1
        else:
            dictAB[sumAB] = 1
            
        sumCD = C[i] + D[j]
        if sumCD in dictCD:
            dictCD[sumCD] += 1
        else:
            dictCD[sumCD] = 1
        
for e in dictAB.keys():
    if -e in dictCD:
        answer += dictAB[e] * dictCD[-e] # dictAB + dictCD의 원소 합이 0이 되는 경우들을 찾는다.
    
print(answer)