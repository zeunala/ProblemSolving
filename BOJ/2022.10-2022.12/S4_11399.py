'''
ATM

입력
첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)

출력
첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.
'''

'''
- 그리디 알고리즘 문제로 보인다. 가장 빨리 걸리는 사람부터 인출하도록 한다.
* Pass/1st/00:04:02
'''
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

currentSum = 0
sumArr = []
for e in arr:
    currentSum += e
    sumArr.append(currentSum)
    
print(sum(sumArr))