'''
수 이어 쓰기 1

입력
첫째 줄에 N(1 ≤ N ≤ 100,000,000)이 주어진다.

출력
첫째 줄에 새로운 수의 자릿수를 출력한다.
'''

'''
- 1~9는 한 자리, 10~99는 두 자리, 100~999는 세 자리, ... 식의 규칙성을 이용한다.
예를 들어 N=23456이면 1~9999까지를 구하고, 이후 13457번에 대해서는 모두 다섯자리이므로 둘의 결과를 더하면 된다.
* Pass/1st/00:08:46
'''

N = int(input())

count = 1 # 현재 써야 하는 수는 몇 개의 자리인지
writeNum = 0 # 지금까지 몇 번째까지 썼는지
idx = 9 # 9, 90, 900, 9000, ... 주기별로 자리수가 하나씩 증가함을 이용
answer = 0

while writeNum + idx < N:
    answer += idx * count
    writeNum += idx
    count += 1
    idx *= 10

answer += (N - writeNum) * count

print(answer)
