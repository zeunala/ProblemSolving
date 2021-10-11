# 알고리즘 문제풀이
주기적으로 알고리즘 문제를 푸는 것을 목표로 하고 있습니다.  
기본적으로 다음 양식에 따라서 작성하고 있습니다.  

>파일명: (문제난이도)_(문제번호/문제이름).(cpp/py 등)  
>  
>(문제 이름)  
>(문제 요약)  
>  
>(문제 접근 방법)  
>(채점 결과 및 문제 풀이 소요시간)  
>(선택 - 문제에 대한 코멘트)  
>  
>[소스 코드]  

\
**예시**
```py
# 파일명: B5_1000.py

'''
A+B

입력
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
첫째 줄에 A+B를 출력한다.
'''

'''
- A, B를 input()으로 입력받아 그 합을 print로 출력하면 되는 문제이다. 
A와 B 사이에 공백을 주고 있으므로 split()을 사용하여 입력받으면 된다.
* Fail/1st/00:03:05
- 문자열의 형태로 입력값이 주어지므로 int로 형변환을 거친 후 더해야 한다.
* Pass/2nd/00:04:06
'''
A, B = map(int, input().split()) # A, B를 입력받아 int형으로 바꾼다.  
print(A+B) # A와 B를 더한 값을 출력한다.
```