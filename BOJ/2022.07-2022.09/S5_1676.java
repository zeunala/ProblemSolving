/*
팩토리얼 0의 개수

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.

- 수를 1부터 곱하되 0이 나올 때마다 뒤에서부터 0을 제거하도록 한다.
* Fail/1st/00:08:39
- 수를 한자리만 남기고 지우면 예를 들어 25*4 = 100이 되어야 할 것이 5*4 = 20이 되어 0의 개수가 줄어들 수 있다.
더 많은 자리수를 남기도록 수정하였다.
* Fail/2nd/00:14:58
- 더 많은 자리수를 남기도록 수정하는 과정에서 곱한 결과가 int범위를 넘어서는 문제가 발생할 수 있다.
long 자료형을 사용하도록 수정하였다.
* Pass/3rd/00:16:44
- 문제를 푼 후 다른 풀이를 본 결과, 10 = 2 * 5에서 착안하여 2와 5가 곱해진 개수를 체크하는 방법도 있음을 알 수 있었다.
*/
import java.util.*;

public class S5_1676 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int answer = 0;
        long temp = 1;

        for (int i = 1; i <= N; i++) {
            temp *= i;

            // 맨 뒤에서부터 0을 제거하고 그 만큼 answer에 기록한다.
            while (temp % 10 == 0) {
                answer++;
                temp /= 10;
            }

            // 너무 자릿수가 많아지지 않도록 수가 길경우 지움
            temp = (temp % 1000000000);
        }
        System.out.println(answer);

        sc.close();
    }
}
