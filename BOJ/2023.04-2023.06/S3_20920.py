'''
영단어 암기는 괴로워

입력
첫째 줄에는 영어 지문에 나오는 단어의 개수 N과 외울 단어의 길이 기준이 되는 M이 공백으로 구분되어 주어진다. (1<=N<=100000, 1<=M<=10)
둘째 줄부터 N+1번째 줄까지 외울 단어를 입력받는다. 이때의 입력은 알파벳 소문자로만 주어지며 단어의 길이는 10을 넘지 않는다.
단어장에 단어가 반드시 1개 이상 존재하는 입력만 주어진다.

출력
화은이의 단어장에 들어 있는 단어를 단어장의 앞에 위치한 단어부터 한 줄에 한 단어씩 순서대로 출력한다.
'''

'''
- 길이가 M이상인 단어들만 필터링하고 우선순위에 따라 정렬하도록 한다.
* Pass/1st/00:05:00
'''
import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().rstrip().split())
dict = defaultdict(int)

for i in range(N):
    wordInput = sys.stdin.readline().rstrip()
    
    if len(wordInput) >= M:
        dict[wordInput] += 1
        
arr = list(dict.keys())
arr.sort(key = lambda x : (-dict[x], -len(x), x))

for e in arr:
    print(e)