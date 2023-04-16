'''
숫자 더하기

입력
한 줄에 하나씩 연습문제가 주어진다.
각 줄에서 첫 번째로 나오는 정수 N (2 ≤ N ≤ 14) 은 연습문제에서 사용될 숫자의 개수이다.
두 번째부터 사용될 N개의 숫자가 주어진다. 0이 아닌 수가 최소 2개 이상 존재한다
마지막 줄에 0을 입력하면 프로그램이 종료된다.

출력
각 연습문제마다 정답을 출력한다.
'''

'''
- 그리디 알고리즘으로 접근한다. 큰 숫자를 최대한 일의 자리쪽으로 몰고, 작은 숫자는 최대한 큰 자리쪽으로 몰아야한다.
N이 짝수일 경우 123456 -> 135 246과 같이 접근하고,
N이 홀수일 경우 1234567 -> 1357 246과 같이 접근한다.
이때 맨앞에 0이 오지 않도록 주의한다.
* Pass/1st/00:16:48
'''
import sys

while True:
    arr = list(sys.stdin.readline().rstrip().split())
    if arr[0] == "0":
        break
    arr = arr[1:]
    arr.sort()
    
    firstNum = ""
    secondNum = ""
    nonZeroIdxStart = arr.count("0") # 0이 아닌 수가 등장하기 시작하는 인덱스
    
    firstNum += arr.pop(nonZeroIdxStart)
    secondNum += arr.pop(nonZeroIdxStart)
    
    for i in range(len(arr)): # 작은 수부터 firstNum -> secondNum 순으로 왔다갔다하며 붙임
        if i % 2 == 0:
            firstNum += arr[i]
        else:
            secondNum += arr[i]
            
    print(int(firstNum) + int(secondNum))