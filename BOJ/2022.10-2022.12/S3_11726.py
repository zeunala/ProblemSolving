'''
2×n 타일링

입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
'''

'''
- f(1) = 1, f(2) = 2, f(n) = f(n-1) + f(n-2) 임을 이용한다.
* Pass/1st/00:03:23
'''
n = int(input())

arr = [0] * (n + 1)

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    arr[1] = 1
    arr[2] = 2
    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    print(arr[n] % 10007)