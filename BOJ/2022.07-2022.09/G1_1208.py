'''
부분수열의 합 2

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 40, |S| ≤ 1,000,000)
둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.
'''

'''
- 음수가 있으므로 투포인터로는 어려워보이며, N의 범위가 작으므로 모든 범위를 계산해보도록 한다.
* Fail/1st/00:05:51
'''
N, S = map(int, input().split())
arr = list(map(int, input().split()))
arrSum = [0] * (len(arr) + 1) # arrSum[i]는 arr[0]~arr[i - 1]까지의 부분합

for i in range(1, len(arrSum)):
    arrSum[i] = arrSum[i - 1] + arr[i - 1]

answer = 0
for i in range(0, len(arrSum)):
    for j in range(i + 1, len(arrSum)):
        if arrSum[j] - arrSum[i] == S:
            answer += 1
            
print(answer)