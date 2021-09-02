'''
괄호 추가하기

입력
첫째 줄에 수식의 길이 N(1 ≤ N ≤ 19)가 주어진다. 둘째 줄에는 수식이 주어진다. 수식에 포함된 정수는 모두 0보다 크거나 같고, 9보다 작거나 같다. 문자열은 정수로 시작하고, 연산자와 정수가 번갈아가면서 나온다. 연산자는 +, -, * 중 하나이다. 여기서 *는 곱하기 연산을 나타내는 × 연산이다. 항상 올바른 수식만 주어지기 때문에, N은 홀수이다.

출력
첫째 줄에 괄호를 적절히 추가해서 얻을 수 있는 결과의 최댓값을 출력한다. 정답은 231보다 작고, -231보다 크다.
'''

'''
- 괄호를 자유롭게 쓸 수 있다는 것은 연산 순서를 마음대로 해도 된다는 뜻이다.
수식의 길이가 19이므로 연산자는 최대 9개, 9!=362880이므로 완전 탐색을 고려해볼 수 있다.
다만 중첩된 괄호가 안된다고 했으므로 i번째 연산자로 연산을 했다면 그 다음부터는 i+2번째 연산자부터 괄호를 묶을 수 있게(먼저 계산이 가능하게) 해야한다.
* Fail/1st/00:58:05/IndexError
- if 2*i+3 >= len(expr) 부분에서 expr[2*i:2*i+3]가 혹시 걸려서 그런건가 싶어 한 번 고쳐보았다.
* Fail/2nd/01:15:25/IndexError
'''
def evaluate(expr): # 원소 3개인 배열을 받아 연산결과를 배열로 리턴(ex. evaluate(['1','+','2'])=['3'])
    if expr[1] == "+":
        return [str(int(expr[0])+int(expr[2]))]
    if expr[1] == "-":
        return [str(int(expr[0])-int(expr[2]))]
    if expr[1] == "*":
        return [str(int(expr[0])*int(expr[2]))]

def allSearch(expr, n, start): # expr은 계산해야할 문자열, n은 남은 연산자 수. 괄호 사용시 start번째의 연산자부터 사용가능(0번째 연산자부터 시작한다 했을 때)

    if n == 1:
        return evaluate(expr)
    maximum = -(2**31)

    # 괄호가 없는 경우
    temp = allSearch(evaluate(expr[0:3])+expr[3:], n-1, max(start-1, 0)) # 연산자 맨 앞에서 하나 빠지므로 괄호 제한도 그에 맞춰 한 칸씩 당겨짐


    if int(temp[0]) > maximum:
        maximum = int(temp[0])

    for i in range(max(start, 1), n): # i번째 연산자에 대해 괄호가 묶인 경우(i번째 연산자는 str[2i+1]에 위치한다.)
        if 2*i+3 >= len(expr): # 마지막 연산자일 경우에 대한 처리
            temp = allSearch(expr[:2*i]+evaluate(expr[2*i:]), n-1, i+1)
        else:
            temp = allSearch(expr[:2*i]+evaluate(expr[2*i:2*i+3])+expr[2*i+3:], n-1, i+1) # i번째 괄호 연산시 i+2번째부터 괄호가능(근데 연산자 하나 없어지므로 새 식에서는 i+1이 기준)

        if int(temp[0]) > maximum:
            maximum = int(temp[0])

    return ([]+[str(maximum)])

N = int(input())
expr = list(input())
print(allSearch(expr, (N-1)//2, 0)[0])