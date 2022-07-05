/*
팩토리얼 0의 개수

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.

- 수를 1부터 곱하되 0이 나올 때마다 뒤에서부터 0을 제거하도록 한다.
* Fail/1st/00:08:39
*/
import java.util.*;

public class S5_1676 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int answer = 0;
        int temp = 1;

        for (int i = 1; i <= N; i++) {
            temp *= i;

            // 맨 뒤에서부터 0을 제거하고 그 만큼 answer에 기록한다.
            while (temp % 10 == 0) {
                answer++;
                temp /= 10;
            }

            // 1의 자리 부분만 남기고 나머지는 지움
            temp = (temp % 10);
        }
        System.out.println(answer);

        sc.close();
    }
}
