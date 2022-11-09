/*
2 타워

입력
입력의 첫째 줄에 높이 H가 주어진다. (1 ≤ H ≤ 10^100)

출력
첫째 줄에 높이가 H인 2 타워의 값을 3으로 나눈 나머지를 출력하라.

- 2의 거듭제곱에서 짝수번 곱해지면 3으로 나눈 나머지는 1이다. (4^n = (3 + 1)^n이므로)
그런데 H>=1 일 때 H 타워의 값은 무조건 짝수이므로, H>=2 이상일 때 2^(짝수)이므로 3으로 나눈 나머지는 1이다.
따라서 H가 1인지 아닌지만 판단하면 된다.
* Pass/1st/00:09:48
*/
import java.util.Scanner;

public class S3_10407 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String H = sc.nextLine();

        if (H.length() == 1 && H.equals("1")) {
            System.out.println(2);
        } else {
            System.out.println(1);
        }
    }
}
