/*
링

입력
첫째 줄에 링의 개수 N이 주어진다. (3 ≤ N ≤ 100)
다음 줄에는 링의 반지름이 상근이가 바닥에 놓은 순서대로 주어진다.
반지름은 1과 1000를 포함하는 사이의 자연수이다.

출력
출력은 총 N-1줄을 해야 한다.
첫 번째 링을 제외한 각각의 링에 대해서, 첫 번째 링을 한 바퀴 돌리면 그 링은 몇 바퀴 도는지 기약 분수 형태 A/B로 출력한다.

- 첫번째 링 / n번째 링을 기약분수로 나타내면 될 것으로 보인다.
* Pass/1st/00:09:09
*/
import java.util.Scanner;

public class S4_3036 {
    public static int gcd(int a, int b) {
        if (a < b) {
            int temp = a;
            a = b;
            b = temp;
        }

        if (a % b == 0)
            return b;
        else
            return gcd(b, a - b);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int base = sc.nextInt();
        
        for (int i = 0; i < N - 1; i++) {
            int target = sc.nextInt();
            System.out.println(base / gcd(base, target) + "/" + target / gcd(base, target));
        }

        sc.close();
    }
}
