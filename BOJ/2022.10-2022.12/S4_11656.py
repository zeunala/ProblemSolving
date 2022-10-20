'''
접미사 배열

입력
첫째 줄에 문자열 S가 주어진다.
S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000보다 작거나 같다.

출력
첫째 줄부터 S의 접미사를 사전순으로 한 줄에 하나씩 출력한다.
'''

'''
- 문자열의 길이가 크지 않으므로 파이썬의 sort를 이용하면 쉽게 구할 수 있을 것이다.
* Pass/1st/00:03:03
'''
S = input()

arr = []

for i in range(len(S)):
    arr.append(S[i:])
arr.sort()

for e in arr:
    print(e)