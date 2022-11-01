'''
에라토스테네스의 체

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ K < N, max(1, K) < N ≤ 1000)

출력
첫째 줄에 K번째 지워진 수를 출력한다.
'''

'''
- N, K의 범위가 크지 않으므로 문제의 요구사항대로 구현하면 되는 문제이다.
* Pass/1st/00:06:21
'''
N, K = map(int, input().split())

deleteNum = []
arr = [False] * (N + 1) # 지워졌는지 여부

for i in range(2, N + 1):
    if arr[i]:
        continue
    
    arr[i] = True
    deleteNum.append(i)
    
    j = 1
    while (i * j <= N):
        if arr[i * j]:
            j += 1
            continue
        
        arr[i * j] = True
        deleteNum.append(i * j)
        
        j += 1

print(deleteNum[K - 1])