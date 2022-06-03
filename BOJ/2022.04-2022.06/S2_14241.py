'''
슬라임 합치기

입력
첫째 줄에 슬라임의 개수 N (2 ≤ N ≤ 100)이 주어진다.

둘째 줄에는 슬라임의 크기가 주어진다. 크기는 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 영선이와 효빈이가 얻을 수 있는 점수의 최댓값을 출력한다.
'''

'''
- 슬라임의 크기가 가장 작은 걸 2개 붙이는 것을 반복하도록 한다.
* Pass/1st/00:06:10
'''
from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0

while len(arr) > 1:
    a = arr.pop()
    b = arr.pop()
    answer += a * b
    arr.insert(bisect_left(arr, a + b), a + b)
    
print(answer)