'''
삼삼한 수

입력
첫째 줄에 2,147,483,647보다 작거나 같은 음이 아닌 정수 N이 입력된다.

출력
입력된 수가 삼삼하다면 YES, 그렇지 않다면 NO를 출력한다.
'''

'''
- 입력된 수를 3진법으로 나타냈을 때 0아니면 1로만 이루어졌는지 판단하면 된다.
* Pass/1st/00:04:24
'''
N = int(input())

if N == 0:
    print("NO")
else:
    while N >= 3:
        if N % 3 >= 2:
            break
        else:
            N //= 3
    
    if N % 3 >= 2:
        print("NO")
    else:
        print("YES")