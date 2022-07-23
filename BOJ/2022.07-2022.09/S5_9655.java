/*
돌 게임

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 1000)

출력
상근이가 게임을 이기면 SK를, 창영이가 게임을 이기면 CY을 출력한다.

- N이 4의 배수이면 후공이, 그렇지 않으면 선공이 이기게 된다.
* Fail/1st/00:02:35
- N이 4k+2꼴일 경우에도 후공이 이기게 된다.
* Pass/2nd/00:04:10
*/
import java.util.*;

public class S5_9655 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        if (N % 4 == 0 || N % 4 == 2) {
            System.out.println("CY");
        } else {
            System.out.println("SK");
        }

        sc.close();
    }
}
