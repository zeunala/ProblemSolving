'''
문자열 폭발

입력
첫째 줄에 문자열이 주어진다. 문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다.
둘째 줄에 폭발 문자열이 주어진다. 길이는 1보다 크거나 같고, 36보다 작거나 같다.
두 문자열은 모두 알파벳 소문자와 대문자, 숫자 0, 1, ..., 9로만 이루어져 있다.

출력
첫째 줄에 모든 폭발이 끝난 후 남은 문자열을 출력한다.
'''

'''
- 파이썬의 replace를 반복해서 호출하면 될 것으로 생각하였으나 문자열이 100만까지라 "a"*500000+"b"*500000, "ab" 같은 경우 시간이 너무 걸린다.
O(N)의 알고리즘이 되도록 문자열 처음부터 쭉 지나가서 검사하는 식으로 구현하였다.
* Fail/1st/00:35:08/TimeOver
'''
import sys

inputString = sys.stdin.readline().rstrip()
bombString = sys.stdin.readline().rstrip()

i = 0
while i < len(inputString)-(len(bombString)-1):
    if inputString[i:i+len(bombString)] == bombString:
        inputString = inputString[:i]+inputString[i+len(bombString):]
        i -= len(bombString)-1 # 터진곳 주변에서 또 터질 수 있으므로 체크
        if i < 0: # 최솟값 보정
            i = 0
    else:
        i += 1

if inputString == "":
    print("FRULA")
else:
    print(inputString)