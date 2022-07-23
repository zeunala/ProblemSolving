/*
걷기

입력
첫째 줄에 집의 위치 X Y와 걸어서 한 블록 가는데 걸리는 시간 W와 대각선으로 한 블록을 가로지르는 시간 S가 주어진다.
X와 Y는 1,000,000,000보다 작거나 같은 음이 아닌 정수이고, W와 S는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 세준이가 집에가는데 걸리는 최소시간을 출력한다.

- 대각선을 최대한 이용하는 경우와 그렇지 않은 경우 두 경우를 세어 최소시간을 계산한다.
* Pass/1st/00:14:20
*/
import java.util.*;

public class S4_1459 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long X = sc.nextLong();
        long Y = sc.nextLong();
        long W = sc.nextLong(); // 한 블록 걸리는 시간
        long S = sc.nextLong(); // 가로지르는 시간

        long case1 = Math.min(X, Y) * S + (Math.max(X, Y) - Math.min(X, Y)) * W; // 대각선 이용
        long case2 = (X + Y) * W; // 대각선 없이 이동
        long case3 = Math.min(X, Y) * S
            + (Math.max(X, Y) - Math.min(X, Y)) / 2 * (2 * S)
            + (Math.max(X, Y) - Math.min(X, Y)) % 2 * W; // case1과 유사하나 2칸을 대각선 2번으로 취급

        System.out.println(Math.min(Math.min(case1, case2), case3));

        sc.close();
    }
}
