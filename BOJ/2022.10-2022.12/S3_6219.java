/*
소수의 자격

입력
세 정수 A, B, D가 주어진다.

출력
주어진 범위 내에서 숫자 D를 포함하는 소수의 개수를 출력한다.

- 소수 목록을 구하고 여기서 숫자 D를 포함하는 소수의 개수를 구한다.
* Pass/1st/00:11:40
*/
import java.util.Arrays;
import java.util.Scanner;

public class S3_6219 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int D = sc.nextInt();
        final int MAX_RANGE = 4000001;
        boolean[] isPrime = new boolean[MAX_RANGE];
        int answer = 0;

        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;

        // 소수 목록을 만든다.
        for (int i = 0; i < (int) Math.ceil(Math.sqrt(MAX_RANGE)) + 1; i++) {
            if (isPrime[i] == false) {
                continue;
            }

            int j = 2;
            while (i * j < MAX_RANGE) {
                isPrime[i * j] = false;

                j++;
            }
        }

        // 소수인 것중 D를 포함하는 것들을 카운트한다.
        for (int i = A; i <= B; i++) {
            int temp = i;
            if (isPrime[i] == false) {
                continue;
            }

            while (temp > 0) {
                if (temp % 10 == D) {
                    answer++;
                    break;
                }
                temp /= 10;
            }
        }
        System.out.println(answer);

        sc.close();
    }
}
