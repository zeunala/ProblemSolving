/*
소수

입력
첫 번째 줄에 A와 B(1 ≤ A, B ≤ 100,000), N(1 ≤ N ≤ 1,000,000)이 공백을 경계로 주어진다.

출력
A÷B를 했을 때, 소숫점 아래 N번째 수를 출력한다.

- 일반 손계산 하는 것과 유사하게 계산하도록 한다.
* Pass/1st/00:04:19
*/
import java.util.*;

public class S5_1312 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int N = sc.nextInt();

        int answer = 0;

        for (int i = 0; i <= N; i++) {
            answer = A / B;
            A %= B;
            A *= 10;
        }
        
        System.out.println(answer);
        sc.close();
    }
}
