'''
성적 통계

입력
첫째 줄에 중덕 고등학교에 있는 반의 수 K (1 ≤ K ≤ 100)가 주어진다.
다음 K개 줄에는 각 반의 학생수 N (2 ≤ N ≤ 50)과 각 학생의 수학 성적이 주어진다.
시험 성적은 0보다 크거나 같고, 100보다 작거나 같은 정수이고, 공백으로 나누어져 있다. 

출력
각 반에 대한 출력은 다음과 같이 두 줄로 이루어져 있다.
첫째 줄에는 "Class X"를 출력한다. X는 반의 번호이며 입력으로 주어진 순서대로 1부터 증가한다.
둘째 줄에는 가장 높은 점수, 낮은 점수, 성적을 내림차순으로 정렬했을 때 가장 큰 인접한 점수 차이를 예제 출력과 같은 형식으로 출력한다.
'''

'''
- 수의 범위가 적으므로 조건에 따라 계산해서 출력하면 된다.
* Pass/1st/00:10:59
'''
K = int(input())

for i in range(1, K + 1):
    tempArr = list(map(int, input().split()))
    del tempArr[0]
    
    tempArr.sort()
    largestGap = tempArr[1] - tempArr[0]
    
    for j in range(1, len(tempArr) - 1):
        if largestGap < tempArr[j + 1] - tempArr[j]:
            largestGap = tempArr[j + 1] - tempArr[j]
    
    print('Class ' + str(i))
    print('Max ' + str(max(tempArr)) + ', Min ' + str(min(tempArr)) + ', Largest gap ' + str(largestGap))