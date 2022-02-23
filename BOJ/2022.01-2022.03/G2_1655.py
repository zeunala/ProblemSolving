'''
가운데를 말해요

입력
첫째 줄에는 백준이가 외치는 정수의 개수 N이 주어진다.
N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다.
그 다음 N줄에 걸쳐서 백준이가 외치는 정수가 차례대로 주어진다.
정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

출력
한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 순서대로 출력한다.
'''

'''
- 각 정수마다 이진탐색을 통해 삽입하고, 중간값을 출력하도록 한다.
* Fail/1st/00:39:43/TimeOver
- 하나 하나 탐색하는 대신 파이썬의 bisect를 이용하는 방식으로 수정하였다.
* Fail/2nd/00:43:27/TimeOver
'''
import sys
from bisect import bisect_left
import random

N = int(sys.stdin.readline().rstrip())

arr = []
arr.append(int(sys.stdin.readline().rstrip())) # 첫번째 수 넣고 시작
print(arr[0])

for i in range(N-1):
    num = int(sys.stdin.readline().rstrip())

    arr.insert(bisect_left(arr, num), num)
    
    if len(arr) % 2 == 0:
        print(min(arr[len(arr)//2], arr[len(arr)//2 - 1]))
    else:
        print(arr[len(arr)//2])
