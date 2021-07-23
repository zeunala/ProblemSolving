'''
단어 수학

입력
첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다. 둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다. 단어는 알파벳 대문자로만 이루어져있다. 모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 수의 최대 길이는 8이다. 서로 다른 문자는 서로 다른 숫자를 나타낸다.

출력
첫째 줄에 주어진 단어의 합의 최댓값을 출력한다.
'''

'''
- 처음엔 알파벳 종류가 최대 10개이므로 각 0~9를 대응하는 10!의 완전 탐색을 이용하려고 했으나,
그냥 최댓값만 구하면 되므로 각 알파벳 별로 곱해지는 수를 구해 비중이 큰 것부터 9, 8, .. 식으로 할당하면 될 것이다.
* Pass/1st/00:39:20
'''

N = int(input())
arr=[] # 각 알파벳들
arrSplit=[] # arr를 알파벳단위로 쪼갠것(중간연산결과)
alphabet=[] # arr에 들어있는 모든 알파벳
alphabetSum={} # (알파벳, 자연수) 쌍으로 들어가는 딕셔너리. (A, 201)은 전부 합 구할 때 A가 총 201번 곱해짐을 의미

for i in range(N):
    temp = input()
    arr.append(temp)
    arrSplit+=list(temp)
alphabet=list(set(arrSplit))
for e in alphabet:
    alphabetSum[e] = 0

for e in arr: # arr에서 단어를 하나 꺼내와서
    idx = 1
    for j in range(len(e)-1, -1, -1): # 단어 맨 뒷자리부터 1, 10, 100을 곱함
        alphabetSum[e[j]] += idx
        idx *= 10

answer = 0
# 이제 alphabetSum에서 가장 비중이 큰 것부터 9, 8, 7... 을 부여한다.
idx = 9
while(alphabetSum):
    tempMax = max(list(alphabetSum.values())) # 가장 비중이 큰 것의 값
    for i in range(len(alphabet)):
        if alphabetSum[alphabet[i]] == tempMax: # 가장 비중이 큰 알파벳을 찾으면
            answer+=(tempMax*idx) # 남아있는 가장 큰 숫자를 곱하고 제거
            del alphabetSum[alphabet[i]]
            del alphabet[i]
            break
    idx -= 1

print(answer)