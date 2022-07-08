'''
회문

입력
입력의 첫 줄에는 주어지는 문자열의 개수를 나타내는 정수 T(1 ≤ T ≤ 30)가 주어진다.
다음 줄부터 T개의 줄에 걸쳐 한 줄에 하나의 문자열이 입력으로 주어진다.
주어지는 문자열의 길이는 3 이상 100,000 이하이고, 영문 알파벳 소문자로만 이루어져 있다.

출력
각 문자열이 회문인지, 유사 회문인지, 둘 모두 해당되지 않는지를 판단하여 회문이면 0, 유사 회문이면 1,
둘 모두 아니면 2를 순서대로 한 줄에 하나씩 출력한다.
'''

'''
- 회문인지 판단하는 함수를 만들고, 여기서 조건이 불일치하는 문자가 있다면 유사 회문인지 판단하는 함수를 호출한다.
* Pass/1st/00:14:08
'''
def checkPalindrome(sentence):
    for i in range(len(sentence)):
        if sentence[i] != sentence[-(i+1)]: # 회문이 아니도록 하는 문자 발견시 그 문자를 빼고 회문인지 확인한다.
            return min(checkPseudoPalindrome(sentence[:i] + sentence[i+1:]), checkPseudoPalindrome(sentence[:len(sentence)-(i+1)] + sentence[len(sentence)-(i+1)+1:]))
    return 0

def checkPseudoPalindrome(sentence):
    for i in range(len(sentence)):
        if sentence[i] != sentence[-(i+1)]: # 여기서도 회문이 아니도록 하는 문자가 발견되면 2를 리턴한다.
            return 2
    return 1

N = int(input())
for i in range(N):
    print(checkPalindrome(input()))