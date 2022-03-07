'''
쉬운 계단 수

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
'''

'''
- N을 점점 늘리면서 계단 수의 개수를 카운팅한다.
이 때 각 계단 수의 첫 자리가 각각 0~9인 것의 개수를 카운팅하여 다음 계단 수 개수를 산정한다.
여기서 첫 자리 0은 계단 수의 개수에 카운팅하면 안되므로 주의하자.
* Pass/1st/00:06:59
'''
N = int(input())

arr = [1 for _ in range(10)]
for i in range(1, N):
    newArr = [0 for _ in range(10)]
    newArr[0] = arr[1]
    for j in range(1, 9):
        newArr[j] = arr[j - 1] + arr[j + 1]
    newArr[9] = arr[8]
    
    arr = newArr[:]
    
print((sum(arr) - arr[0])%int(1e9))