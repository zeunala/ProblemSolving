'''
보물

입력
첫째 줄에 N이 주어진다.
둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어진다.
N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.

출력
첫째 줄에 S의 최솟값을 출력한다.
'''

'''
- S의 최솟값만 구하면 되므로 A와 B를 각각 내림차순, 오름차순으로 정렬하고 둘을 곱하면 S의 최솟값이 나오게 된다.
* Pass/1st/00:03:10
'''
N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort(reverse=True)

S = 0
for i in range(N):
    S += arr1[i] * arr2[i]
print(S)