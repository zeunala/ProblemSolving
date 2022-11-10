'''
큰 수 만들기

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 리스트에 포함된 수가 주어진다.
수는 공백으로 구분되어져 있고, 1,000,000,000보다 작거나 같은 음이 아닌 정수이다.
0을 제외한 나머지 수는 0으로 시작하지 않으며, 0이 주어지는 경우 0 하나가 주어진다.

출력
리스트에 포함된 수를 나열하여 만들 수 있는 가장 큰 수를 출력한다.
수는 0으로 시작하면 안되며, 0이 정답인 경우 0 하나를 출력해야 한다.
'''

'''
- 버블소트를 하되 둘 중 큰 수의 기준을 다음과 같이 바꾼다.
A, B중 숫자를 그대로 이은 AB, BA를 만들어 AB가 크다면 A가, BA가 크다면 B가 큰 걸로 한다.
ex. 353와 35의 경우 35335 < 35353 이므로 35가, 353과 3의 경우 3533 > 3353 이므로 353이 더 큰 걸로 한다. 
* Fail/1st/00:38:23
'''
def isRightBigger(a, b): # a < b이면 True, 그렇지 않으면 False 리턴 (a와 b는 문자열)
    if a + b < b + a:
        return True
    else:
        return False
    
N = int(input())
arr = list(input().split())
    
for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):
        if isRightBigger(arr[j], arr[j + 1]): # 문자열이 가장 작은게 뒤로 오도록 정렬
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
for e in arr:
    print(e, end = "")