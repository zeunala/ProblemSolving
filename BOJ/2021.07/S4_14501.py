'''
퇴사

입력
첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

출력
첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.
'''

'''
- N일째부터 시작했을 때의 최대 이익을 구하고 N-1, N-2, ... 1일째부터 시작했을 때의 최대 이익을 구한다.
N-A일째부터 시작했을 때 최대 이익은, N-A+1일째 시작시 최대 이익 vs N-A+T일째 시작시 최대 이익+P 이다.
이 때 날짜가 N을 초과하지 않도록 조심하자
* Pass/1st/00:15:40
'''
N = int(input())
T = [0] # 계산 편의를 위해 인덱스 1부터 시작
P = [0] # 계산 편의를 위해 인덱스 1부터 시작
for i in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

maxP = [0] # maxP[i]는 i일째(i>=1) 시작했을때 최대 이익
for i in range(N):
    maxP.append(0)
maxP.append(0) # 끝에 0을 하나 더 넣음(N일째 계산할 때 N+1일째의 값에 접근하는 경우 때문)

for i in range(N, 0, -1): # N일째부터 시작했을 때의 최대 이익부터 구해나감
    if(i+T[i]>N+1): # 퇴사 기간을 넘어가는 경우는 고려 안함
        maxP[i]=maxP[i+1]
    else:
        maxP[i]=max(maxP[i+1], maxP[i+T[i]]+P[i])

print(maxP[1])