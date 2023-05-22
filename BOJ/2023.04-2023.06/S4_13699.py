'''
점화식

입력
첫째 줄에 n (0 ≤ n ≤ 35)이 주어진다.

출력
첫째 줄에 t(n)을 출력한다.
'''

'''
- 문제의 요구사항을 그대로 구현하되 이미 계산한 t(n)값을 중복 계산하지 않도록 저장한다.
* Pass/1st/00:04:53
'''
n = int(input())

tArr = [1] # tArr[i]는 t(i)값

for i in range(1, n + 1): # t(1)부터 t(n)값까지를 구한다.
    result = 0
    for j in range(i):
        result += tArr[j] * tArr[i - 1 - j]
    tArr.append(result)
    
print(tArr[-1])