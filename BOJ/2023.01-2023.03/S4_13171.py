'''
A

입력
첫 번째 줄에는 정수 A(1 ≤ A ≤ 10^18)이 주어진다.

두 번째 줄에는 정수 X(1 ≤ X ≤ 10^18)가 주어진다.

출력
A^X을 출력한다. 이 수는 매우 커질 수 있으므로 1,000,000,007로 나눈 나머지를 출력해야 한다.
'''

'''
- 문제에서 제시한 방법대로 X의 이진수를 구해 이를 이용해 A^X를 계산한다.
2 ** 60 > 10 ** 18 이므로 A^(2**60)까지의 값을 미리 계산해둔다.
* Pass/1st/00:15:27
'''
A = int(input())
X = int(input())
mod = 1000000007

valueDict = {} # valueDict[x] = y라면 A^(2 ** x) = y임을 의미

currentValue = A % mod
valueDict[1] = currentValue
for i in range(2, 61):
    currentValue = ((currentValue % mod) * (currentValue % mod)) % mod
    valueDict[i] = currentValue
    
currentX = X
answer = 1
idx = 1 # A^1 부터 A^2, A^4, ... 순으로 해당 수가 곱해지는 것이 있는지 체크한다.
while currentX > 0:
    if currentX % 2 == 1:
        answer = ((answer % mod) * (valueDict[idx] % mod)) % mod
        
    idx += 1
    currentX //= 2
    
print(answer)