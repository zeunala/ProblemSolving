'''
수열 정렬

입력
첫째 줄에 배열 A의 크기 N이 주어진다.
둘째 줄에는 배열 A의 원소가 0번부터 차례대로 주어진다.
N은 50보다 작거나 같은 자연수이고, 배열의 원소는 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 비내림차순으로 만드는 수열 P를 출력한다.
'''

'''
- 정렬된 배열을 하나 더 만들어 기존 배열이 정렬된 배열의 어느 인덱스에 위치하는지 체크한다.
* Pass/1st/00:07:58
- 원래는 맨 마지막 공백을 제외해야하나 마지막에 들어간 공백의 경우 무시하고 채점하는 것으로 보인다. 
'''
N = int(input())
arr = list(map(int, input().split()))
arrSorted = arr[:]
arrSorted.sort()

answer = []
for e in arr:
    targetIndex = arrSorted.index(e)
    answer.append(targetIndex)
    arrSorted[targetIndex] = None # 중복 원소 고려
    
for e in answer:
    print(e, end = " ")