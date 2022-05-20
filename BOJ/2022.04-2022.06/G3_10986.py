'''
나머지 합

입력
첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 10^6, 2 ≤ M ≤ 10^3)

둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 10^9)

출력
첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.
'''

'''
- A1부터 Ai까지의 부분 구간의 합을 M으로 나눈 나머지를 Si로 저장해 놓자.
그렇게 되면 1~N에 대해서 Si-Sj 가 0이 되는 경우가 몇 개인지 세면 된다.
* Pass/1st/00:17:46
'''
from collections import defaultdict
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arrA = list(map(int, sys.stdin.readline().rstrip().split()))
arrS = []
dict = defaultdict(int) # i에 대해서 arrS[0]~arrS[i-1]까지의 나머지들의 개수를 저장하기 위함 

temp = 0
for i in range(len(arrA)):
    temp += arrA[i]
    temp %= M
    arrS.append(temp)
    
answer = 0
for i in range(len(arrS)):
    if arrS[i] == 0:
        answer += 1  # arrA[0]~arrA[i]까지의 부분합이 M으로 나누어 떨어지는 경우
    
    # arrA[0]~arrA[i]까지의 부분합 % M = n이고 arrA[0]~arrA[j]까지의 부분합 % M = n이라면,
    # arrA[j+1]~arrA[i]까지의 부분합 역시 M으로 나누어 떨어진다.
    answer += dict[arrS[i]]
    
    dict[arrS[i]] += 1

print(answer)