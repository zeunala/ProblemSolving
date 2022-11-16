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
- 1, 1 1 뿐만 아니라 1만 있는 상황 모두가 예외상황에 속한다.
따라서 모든 숫자가 1일 때, 1의 개수가 홀수개라면 후공이, 1의 개수가 짝수개라면 선공이 승리한다.
* Pass/2nd/00:15:13
- 님 게임을 이전에 알고 있었기에 어렵지 않게 풀 수 있었지만,
문제 풀이 이후 다른 사람의 풀이를 본 결과 이런류의 게임을 일반화하여 스프라그-그런디 정리를 이용할 수 있음을 알게 되었다.
'''
N = int(input())
arr = list(map(int, input().split()))

resultXOR = 0
isAllOne = True
for i in range(len(arr)):
    resultXOR ^= arr[i]
    if arr[i] != 1:
        isAllOne = False

if isAllOne: # 모든 숫자가 1인 상황에서는 resultXOR이 1 아니면 0 이 되므로 ^=1을 해주면 승리자가 바뀌게 된다.
    resultXOR ^= 1
    
if resultXOR != 0:
    print("koosaga")
else:
    print("cubelover")