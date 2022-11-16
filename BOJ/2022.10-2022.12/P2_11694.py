'''
님 게임

입력
첫째 줄에 돌 더미의 개수 N (1 ≤ N ≤ 100)이 주어진다.
둘째 줄에는 각 돌 더미에 쌓여있는 돌의 개수 Pi (1 ≤ Pi ≤ 2×10^9)가 주어진다.

출력
koosaga가 이기는 경우에는 'koosaga'를, cubelover가 이기는 경우에는 'cubelover'를 출력한다.
'''

'''
- 님 게임 문제의 필승법은 각 돌 더미의 개수를 모두 XOR연산하고, 그것을 전부 0으로 되도록 만드는 것이다.
이미 XOR연산의 결과가 0이라면 후공이 승리, 그렇지 않다면 선공이 승리한다.
다만, 예외적으로 1 하나만 있으면 후공이, 1 두 개가 있으면 선공이 승리한다.
* Fail/1st/00:08:45
'''
N = int(input())
arr = list(map(int, input().split()))

resultXOR = 0
for i in range(len(arr)):
    resultXOR ^= arr[i]
    
if len(arr) == 1 and arr[0] == 1:
    print("cubelover")
elif (len(arr) == 2 and arr[0] == 1 and arr[1] == 1) or (resultXOR != 0):
    print("koosaga")
else:
    print("cubelover")