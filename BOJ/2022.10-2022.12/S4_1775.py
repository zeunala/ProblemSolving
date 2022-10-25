'''
숫자놀이

입력
첫째 줄에 M과 N이 주어진다.

출력
M 이상 N 이하의 정수를 문제 조건에 맞게 정렬하여 한 줄에 10개씩 출력한다.
'''

'''
- M, N의 범위가 작으므로 문제의 요구사항대로 그대로 구현하면 되는 문제이다.
* Pass/1st/00:05:47
'''
def numToWord(num):
    numArr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = ""
    
    if num >= 10:
        result += numArr[num // 10] + " "
    result += numArr[num % 10]
    
    return result
    
M, N = map(int, input().split())

arr = [] # (사전으로 읽은 수, 원래 숫자)의 튜플

for i in range(M, N + 1):
    arr.append((numToWord(i), i))
arr.sort()

for i in range(len(arr)):
    if i % 10 == 9 or i == len(arr) - 1: # 10줄씩 끊음
        print(arr[i][1])
    else:
        print(arr[i][1], end = " ")