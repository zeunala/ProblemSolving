'''
두 수의 합

입력
첫째 줄에 수열의 크기 n이 주어진다.
다음 줄에는 수열에 포함되는 수가 주어진다.
셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

출력
문제의 조건을 만족하는 쌍의 개수를 출력한다.
'''

'''
- 서로 다른 양의 정수로 이루어졌다고 했으므로 집합 자료형을 이용하여 각 경우마다 O(1)에 찾도록 한다.
* Pass/1st/00:06:08
'''
import sys

n = int(sys.stdin.readline().rstrip()) # 수열의 크기
arr = list(map(int, sys.stdin.readline().rstrip().split()))
x = int(sys.stdin.readline().rstrip())

arrSet = set(arr) # arr을 집합 자료형으로 만든 것

answer = 0
for e in arr:
    target = x - e # 이 수가 arrSet이 있을 경우 조건을 만족하는 쌍이 된다.
    if target == e: # 서로 다른 정수로 이루어졌다고 했으므로 찾는 값이 e와 같으면 안된다.
        continue
    if target in arrSet:
        answer += 1
        
answer //= 2 # (a, b)와 (b, a)는 같은 경우이므로 2로 나눠준다. (a, a)인 경우는 생각할 필요가 없다.
print(answer)