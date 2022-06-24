/*
GCD 합

입력
첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있다.
각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 다음에는 n개의 수가 주어진다.
입력으로 주어지는 수는 1,000,000을 넘지 않는다.

출력
각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.

- 개수가 많지 않으므로 가능한 모든 쌍에 대하여 하나하나 구하도록 한다.
* Fail/1st/00:11:29
*/
import java.util.*;

public class S3_9613 {
    public static int gcd(int a, int b) {
        if (a < b) {
            int temp = a;
            a = b;
            b = temp;
        }

        if (a % b == 0)
            return b;
        else
            return gcd(b, a % b);

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            int result = 0;

            for (int j = 0; j < n; j++)
                arr[j] = sc.nextInt();

            for (int j = 0; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    result += gcd(arr[j], arr[k]);
                }
            }

            System.out.println(result);
        }

        sc.close();
    }
}
