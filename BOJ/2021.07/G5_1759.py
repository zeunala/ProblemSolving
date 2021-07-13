'''
암호 만들기

입력
첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15) 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다. 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

출력
각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.
'''

'''
- L, C의 범위가 작아 브루트 포스로 충분히 풀 수 있을 듯 하다.
조합으로 모든 경우의 수 다 찾아오고 그 중 모음1개+자음2개 이상인 것만 취하면 쉽게 구할 수 있을 것이다.
* Pass/1st/00:20:55
'''
from itertools import combinations ## 조합이용

def checking(arr): # 자음이 2개이상, 모음이 1개이상이면 true
    a=0 # 자음개수
    b=0 # 모음개수

    for i in arr:
        if 'a'!=i and 'e'!=i and 'i'!=i and 'o'!=i and 'u'!=i:
            a+=1
        else:
            b+=1
    
    return (a>=2 and b>=1)

def sumWord(arr): # 각 배열의 문자를 문자열로 합친다
    result=""
    for i in arr:
        result+=i
    return result
    
L, C=map(int, input().split())
alphabet=list(input().split())
alphabet.sort() # a,b,c순 정렬
allWays=list(combinations(alphabet,L)) ## 일단 모든 경우의 수를 다 구해본다.

for i in allWays: # 각 경우에 대해 조건 충족시 print
    if(checking(i)):
        print(sumWord(i))