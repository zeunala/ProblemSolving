'''
기둥과 보 설치

- 문제에서 제시한 그대로 구현해보자.
전체 벽면을 배열로 만들고 field[y][x]는 (x,y)에 기둥(2)이 있는지 보(1)가 있는지를 나타내게 한다.
만약 둘 다 있으면 3, 둘 다 없으면 0이 오도록 한다.
field[y][x] % 2 == 1 이면 보가 있는 것이고, field[y][x] // 2 == 1이면 기둥이 있는 것이다.
* Fail/1st/00:45:10
'''

def solution(n, build_frame):
    answer = []
    
    n = n + 1 # n = 5기준 (5,5)좌표까지 있으므로 n을 하나 더하고 시작함.
    field = [[0 for i in range(n)] for j in range(n)]
    

    for e in build_frame:
        x, y, a, b = e
        
        if b == 1: # 설치
            if a == 0: # 기둥 설치
                if y == 0 or (x-1 >= 0 and field[y][x-1] % 2 == 1) or (field[y][x] // 2 == 1) or (y-1 >= 0 and field[y-1][x] // 2 == 1): # 기둥 조건 3개중 하나 충족시
                    if field[y][x] // 2 != 1: # 기둥 없다면 기둥을 세운다.
                        field[y][x] += 2
                else: # 조건 충족 안하면 현재 명령 무시하고 다음 명령으로
                    continue
            elif a == 1: # 보 설치
                if (y-1 >= 0 and field[y-1][x] // 2 == 1) or (y-1 >= 0 and x+1 < n and field[y-1][x+1]) or (x-1 >= 0 and x+1 < n and field[y][x-1] % 2 == 1 and field[y][x+1] % 2 == 1): # 보 조건 2개 중 하나 충족시
                    if field[y][x] % 2 != 1: # 보가 없다면 보를 세운다.
                        field[y][x] += 1
                else:
                    continue
                    
        elif b == 0: # 삭제 (단순히 삭제한다 쳤을 때 그 지점/상/하/좌/우 모두 확인해보자)
            # 일단 삭제해보고 조건 안맞으면 롤백시킨다.
            # 없는 구조물을 삭제하는 경우는 입력으로 주어지지 않는다고 하였다.
            minusValue = 0
            valid = True
            if a == 0: # 기둥 삭제
                minusValue = 2
            elif a == 1: # 보 삭제
                minusValue = 1
            field[y][x] -= minusValue
            
            tempValues = [(x, y), (x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
            for (tempX, tempY) in tempValues:
                if field[tempY][tempX] // 2 == 1: # 기둥있을 때 뺀 field 에서도 유효한지
                    if tempY == 0 or (tempX-1 >= 0 and field[tempY][tempX-1] % 2 == 1) or (field[tempY][tempX] // 2 == 1) or (tempY-1 >= 0 and field[tempY-1][tempX] // 2 == 1):
                        pass
                    else:
                        valid = False
                if field[tempY][tempX] % 2 == 1: # 보 있을 때 뺀 field에서도 유효한지
                    if (tempY-1 >= 0 and field[tempY-1][tempX] // 2 == 1) or (tempY-1 >= 0 and tempX+1 < n and field[tempY-1][tempX+1]) or (tempX-1 >= 0 and tempX+1 < n and field[tempY][tempX-1] % 2 == 1 and field[tempY][tempX+1] % 2 == 1):
                        pass
                    else:
                        valid = False
                
                if valid == False:
                    break
                    
            if valid == False: # 조건 안맞은 경우가 발생했다면 롤백
                field[y][x] += minusValue
            
    print(field)
    for x in range(n):
        for y in range(n):
            if field[y][x] // 2 == 1: # 기둥이 있을 경우
                answer.append([x, y, 0])
            if field[y][x] % 2 == 1: # 보가 있을 경우
                answer.append([x, y, 1])
    
    return answer