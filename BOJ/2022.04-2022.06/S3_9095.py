'''
1, 2, 3 더하기

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.
n은 양수이며 11보다 작다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
'''

'''
- n의 범위가 작으므로 재귀함수를 이용하여 쉽게 구할 수 있을 것으로 보인다.
* Pass/1st/00:09:58
'''
def func(n):
    if n < 1:
        return 0
    elif n == 1: # 1 = 1
        return 1
    elif n == 2: # 2 = 2, 1 + 1
        return 2
    elif n == 3: # 3 = 3, 1 + 2, 2 + 1, 1 + 1 + 1
        return 4
    else:
        return func(n - 3) + func(n - 2) + func(n - 1) # 1 + 나머지, 2 + 나머지, 3 + 나머지
    
arr = [func(i) for i in range(11)]
T = int(input())
for i in range(T):
    nextInput = int(input())
    print(arr[nextInput])