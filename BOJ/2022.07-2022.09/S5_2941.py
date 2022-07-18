'''
크로아티아 알파벳

입력
첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

출력
입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
'''

'''
- 입력 길이가 적으므로 문제의 조건을 그대로 구현하도록 한다.
* Pass/1st/00:05:01
'''
inputStr = input()
answer = 0

i = 0
while i < len(inputStr):
    if inputStr[i:i+3] == "dz=":
        answer += 1
        i += 3
    elif inputStr[i:i+2] in ["c=", "c-", "d-", "lj", "nj", "s=", "z="]:
        answer += 1
        i += 2
    else:
        answer += 1
        i += 1

print(answer)