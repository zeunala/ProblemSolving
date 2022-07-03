/*
거듭제곱

입력
첫째 줄에 N이 주어진다. N은 500,000,000,000 이하의 자연수이다.

출력
첫째 줄에 한 개 이상의 서로 다른 3의 제곱수의 합으로 표현되는 N번째로 작은 수를 출력한다.

- 결국 10진수 N을 2진수로 바꾸고, 이를 그대로 3진수로 보아 10진수로 바꾸면 되는 문제와 같다.
* Fail/1st/00:03:50
*/
import java.util.Scanner;

public class S4_1740 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int answer = 0;
        int idx = 1;

        while (N > 0) {
            answer += idx * (N % 2);
            N /= 2;
            idx *= 3;
        }

        System.out.println(answer);
        sc.close();
    }
}
