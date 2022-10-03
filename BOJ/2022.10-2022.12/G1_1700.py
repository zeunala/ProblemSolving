'''
멀티탭 스케줄링

입력
첫 줄에는 멀티탭 구멍의 개수 N (1 ≤ N ≤ 100)과 전기 용품의 총 사용횟수 K (1 ≤ K ≤ 100)가 정수로 주어진다.
두 번째 줄에는 전기용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다.
각 줄의 모든 정수 사이는 공백문자로 구분되어 있다. 

출력
하나씩 플러그를 빼는 최소의 횟수를 출력하시오. 
'''

'''
- 플러그를 빼기 전 최대한 늦게 이용될 전기용품을 교체하도록 한다.
* Fail/1st/00:16:11
'''
N, K = map(int, input().split()) # N: 멀티탭 구멍의 개수, K: 전기 용품의 총 사용횟수
arr = list(map(int, input().split()))

answer = 0
currentPlug = [] # 현재 사용중인 전기용품 번호
nextUseDict = {} # nextUseDict[i]는 i번 전기용품이 다음에 몇 번째로 사용되는지를 보관한다.
INF = 10**10

for i in range(K):
    if arr[i] in currentPlug: # 이미 멀티탭에 연결중인 상황이면 상관이 없다.
        continue
        
    if len(currentPlug) < N: # 멀티탭 구멍 개수가 남으면 일단 꽂는다
        currentPlug.append(arr[i])
    else: # 자리가 부족한 경우
        currentPlug.sort(key = lambda x : -nextUseDict[x]) # 다음에 가장 늦게 사용되는 걸 맨 앞에 오도록 arr을 재배열한다.
        currentPlug[0] = arr[i]
        answer += 1
        
    # 플러그에 꽂으면서 다음에 몇 번째로 사용되는지도 저장해둔다
    if arr[i] in arr[i+1:]:
        nextUseDict[arr[i]] = (i + 1) + arr[i+1:].index(arr[i])
    else:
        nextUseDict[arr[i]] = INF
            
print(answer)