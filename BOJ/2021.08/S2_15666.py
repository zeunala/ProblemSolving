'''
N과 M (12)

입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''

'''
- N, M의 범위가 작으므로 조건에 주의하여 하나씩 계산하면 될 것이다.
* Pass/1st/00:16:26
'''
answer = []

def findAnswer(acc, arr, M): # arr에 있는 숫자 중 M개를 택함. 현재 선택중인 것은 acc에 저장
    if M == 0:
        if acc not in answer:
            answer.append(acc) # 중복제거 위함
        return
    
    for i in range(len(arr)):
        findAnswer(acc+[arr[i]], arr[i:], M-1) # acc 뒤에는 arr[i]를 더하고, arr범위가 줄어들며, 택해야하는 수가 M-1로 감소


N, M = map(int, input().split())
arr = list(set(map(int, input().split()))) # set로 중복제거
arr.sort() # 오름차순 정렬

findAnswer([], arr, M)

for e in answer:
    for e2 in e:
        print(e2, end = " ")
    print()