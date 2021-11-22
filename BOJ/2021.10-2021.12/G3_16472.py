'''
고냥이

입력
첫째 줄에는 인식할 수 있는 알파벳의 종류의 최대 개수 N이 입력된다. (1 < N ≤ 26)
둘째 줄에는 문자열이 주어진다. (1 ≤ 문자열의 길이 ≤ 100,000) 단, 문자열에는 알파벳 소문자만이 포함된다.

출력
첫째 줄에 번역기가 인식할 수 있는 문자열의 최대길이를 출력한다. 
'''

'''
- start = 0, end = 0부터 시작해서 문자열을 처음부터 end를 늘려가며 스캔해본다. 만약 최대 종류가 넘게 되면 start를 늘려 문자열을 줄인다.
* Pass/1st/00:14:36
'''
def alphaAdd(alphabet):
    global alphaArr, differentAlpha
    alphaArr[alphabet] += 1
    if alphaArr[alphabet] == 1:
        differentAlpha += 1
        
def alphaSub(alphabet):
    global alphaArr, differentAlpha
    alphaArr[alphabet] -= 1
    if alphaArr[alphabet] == 0:
        differentAlpha -= 1
    
import sys

N = int(input())
arr = list(sys.stdin.readline().rstrip())

start = 0
end = 0

answer = 0

alphaArr = {}
for e in "abcdefghijklmnopqrstuvwxyz":
    alphaArr[e] = 0
differentAlpha = 0 # 알파벳 종류의 개수

alphaAdd(arr[0])
while end + 1 < len(arr):
    end += 1
    alphaAdd(arr[end])
    while differentAlpha > N: # 최대 인식 알파벳 종류 넘은 경우 start증가
        alphaSub(arr[start])
        start += 1
    if end - start + 1 > answer:
        answer = end - start + 1
        
print(answer)