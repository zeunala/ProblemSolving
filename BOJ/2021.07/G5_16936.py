'''
나3곱2

입력
첫째 줄에 수열의 크기 N(2 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 수열 B가 주어진다. B에 포함된 원소는 1018 보다 작거나 같은 자연수이다.

출력
나3곱2 게임의 결과 수열 A를 출력한다. 항상 정답이 존재하는 경우에만 입력으로 주어지며, 가능한 정답이 여러가지인 경우에는 아무거나 출력한다.
'''

'''
- 수열의 크기가 100이하이므로 각 숫자에 대해 하나하나 확인하는 방법을 사용해도 시간초과 없이 해결할 수 있을 것이다.
* Pass/1st/00:39:28
'''

N = int(input())
arr = list(map(int, input().split()))

isOK = False # 조건에 맞는걸 꺼내왔을 때 나머지 볼 필요 없이 다음 i로 넘어가게 하기 위함

for i in range(1, N): # arr[i-1]까지 나3곱2 조건을 만족한 상태
    isOK = False
    for j in range(i, N): # 조건 만족되지 않은 오른쪽에서 하나를 꺼내온다.
        if(isOK): break

        if(arr[0]*3==arr[j] or arr[0]==arr[j]*2): # 맨 왼쪽에 들어갈 수 있는지 확인
            temp = arr[j]
            del(arr[j])
            arr.insert(0, temp)
            isOK = True
        
        if(arr[j]*3==arr[i-1] or arr[j]==arr[i-1]*2): # 맨 오른쪽에 들어갈 수 있는지 확인
            temp = arr[j]
            del(arr[j])
            arr.insert(i, temp)
            isOK = True

        for k in range(0, i-1): # 두 개 사이에 들어갈 수 있는지 확인(왼쪽 오른쪽 모두 조건을 확인해야 한다) arr[k]와 arr[k+1]사이에 들어갈 수 있는지 체크한다.
            if((arr[k]*2==arr[j] or arr[k]==arr[j]*3) and (arr[j]*2==arr[k+1] or arr[j]==arr[k+1]*3)):
                temp = arr[j]
                del(arr[j])
                arr.insert(k+1, temp)
                isOK = True

for e in arr:
    print(e, end=" ")