'''
IQ 테스트

입력
첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다.
둘째 줄에는 N개의 수가 주어진다. 이 수는 모두 절댓값이 100보다 작거나 같은 정수이다.

출력
다음 수를 출력한다. 만약 다음 수가 여러 개일 경우에는 A를 출력하고, 다음 수를 구할 수 없는 경우에는 B를 출력한다.
'''

'''
- 절댓값이 작아 처음에 완전탐색을 하려고 했으나 a, b가 200이상의 큰 수가 나올 수 있기에 범위를 한정짓기 애매하다.
첫번째 수가 x이면 두번째 수는 ax+b, 세번째 수는 a(ax+b)+b=a^2x+ab+b, 네번째는 a^3x+a^2b+ab+b, ...
두번째수-첫번째수는 ax+b-x
세번째수-두번째수는 a^2x+ab-ax=a(ax+b-x)
네번째수-세번째수는 a^2(ax+b-x) 
와 같은 특성을 이용한다.
* Fail/1st/00:25:08
- a, b가 정수라는 조건을 빠뜨렸다. 공비가 정수라는 가정을 하고 r을 잡았는데 a가 정수가 아니여도 답이 안되도록 수정하였다.
* Pass/2nd/00:41:56
'''
N = int(input())
arr = list(map(int, input().split()))

if N == 1: # 원소가 한 개뿐이면 경우의 수는 매우 많다.
    print('A')
elif N == 2: # 원소가 두 개인 경우
    if arr[0] == arr[1]: # 두 수가 같다면 a,b가 어떻게 되든 다음에 나올 수는 그대로이다.
        print(arr[0])
    else: # 그 외의 경우 x, y가 있을 때 a=0, b=y가 될 수도 있고 a=1, b=y-x가 될 수 있는 등 경우의 수가 많다.
        print('A')
else:
    if arr[0] == arr[1]: # 첫 두 개의 수가 같다면 나머지 수도 모두 같아야하며, 그렇지 않다면 답이 없다.
        isValid = True
        for i in range(2, len(arr)):
            if arr[i] != arr[0]:
                isValid = False
                
        if isValid:
            print(arr[0])
        else:
            print('B')
    else:
        tempArr = [arr[i+1]-arr[i] for i in range(len(arr)-1)] # 이 배열은 a가 곱해지는 등비수열이 된다.
        
        isValid = True # 공비가 모두 일치하는지, 또 그것이 정수인지 체크
        
        r = tempArr[1] // tempArr[0] # r은 공비 (앞에서 첫 두 개의 수가 같은 경우를 걸렀으므로 0으로 나눌 일은 없다)
        if tempArr[0] * r != tempArr[1]: # 공비가 정수가 안 될 경우 여기 걸린다.
            isValid = False
        
        for i in range(1, len(tempArr) - 1):
            if tempArr[i] * r != tempArr[i+1]:
                isValid = False
                
        if isValid:
            tempArr.append(tempArr[-1]*r) # 항을 새로 하나 추가
            print(arr[-1]+tempArr[-1])
        else:
            print('B')