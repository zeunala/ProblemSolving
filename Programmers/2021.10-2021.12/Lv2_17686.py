'''
파일명 정렬

- 정규표현식을 사용하지 않고 작성해보기로 하였다.
각 파일명에 대해 HEAD/NUMBER/IDX로 나누어 sort를 사용한다.
IDX는 입력으로 주어진 files배열에서의 처음 idx로 같은 결과에 대한 순서를 유지하기 위함이다.
* Pass/1st/00:19:27
'''
def solution(files):
    answer = []
    arr = []
    
    # files의 각 문자에 대하여 arr에 넣음
    for i in range(len(files)):
        head = ""
        number = 0
        
        # 숫자가 나오는 것 앞까지 잘라서 HEAD에 넣음
        for j in range(len(files[i])):
            if files[i][j] in "0123456789":
                head = files[i][:j]
                
                # 그 이후 부분부터 숫자를 다 뽑아서 NUMBER에 넣음
                for k in range(j, len(files[i])):
                    if k == len(files[i]) - 1:
                        number = int(files[i][j:])
                        break
                        
                    elif files[i][k] not in "0123456789" or k == len(files[i]) - 1 or k - j >= 5:
                        number = int(files[i][j:k])
                        break
                        
                break
        
        arr.append((head.lower(), number, i))
                
    # arr 정렬
    arr.sort()
    
    # arr의 idx를 기준으로 files배열의 원소들을 정렬 순서에 맞게 answer에 옮김
    for e in arr:
        (head, num, idx) = e
        answer.append(files[idx])
        
    return answer