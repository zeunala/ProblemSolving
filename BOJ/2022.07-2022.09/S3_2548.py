'''
대표 자연수

입력
첫째 줄에는 자연수의 개수 N이 입력된다.
N은 1 이상 20,000 이하이다.
둘째 줄에는 N개의 자연수가 빈칸을 사이에 두고 입력되며, 이 수들은 모두 1 이상 10,000 이하이다.

출력
첫째 줄에 대표 자연수를 출력한다.
대표 자연수가 두 개 이상일 경우 그 중 제일 작은 것을 출력한다.
'''

'''
- 결국 중앙값을 구하는 문제로 보인다. 주어진 수가 짝수개라면 가운데 두 수 중 작은 수를 출력하도록 한다.
* Pass/1st/00:03:28
'''
N = int(input())
arr = list(map(int, input().split()))

arr.sort()

if N % 2 == 1:
    print(arr[N // 2])
else:
    print(arr[N // 2 - 1])