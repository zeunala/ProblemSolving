'''
최대 곱

입력
첫째 줄에 두 수 S와 K가 주어진다. K는 20보다 작거나 같고, S는 100보다 작거나 같으며 K보다 크거나 같다.

출력
첫째 줄에 정답을 출력한다. 답은 9223372036854775807보다 작다.
'''

'''
- 양의 정수를 최대한 균등하게 나눠야 최대 곱이 나온다는 점을 이용한다.
* Pass/1st/00:07:09
'''
S, K = map(int, input().split()) # K개의 양의 정수 합이 S

numArr = [0] * K

for i in range(K):
    numArr[i] = S // K
    
    # 나머지가 있는 경우 앞에서부터 균등하게 배분 (ex. S = 7, K = 5일 때 2 2 1 1 1)
    if S % K >= i + 1:
        numArr[i] += 1
    
answer = 1
for e in numArr:
    answer *= e
print(answer)