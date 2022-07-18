/*
짝수? 홀수?

입력
첫 번째 줄에는 전체 테스트 개수 (N) 가 주어진다. (1 ≤ N ≤ 100)
두 번째 줄에는 약수 개수를 판별할 수 (X) 가 주어진다 (1 ≤ X ≤ 10^18).

출력
주어진 수의 약수 개수가 홀수이면 1, 짝수이면 0 을 출력하시오.

- 주어진 수가 어떤 수의 제곱이면 약수 개수가 홀수이고, 짝수이면 0이 될 것이다.
* Fail/1st/00:05:17
- 큰 수가 입력으로 주어질 때도 생각하도록 한다.
* Pass/2nd/00:11:46
*/
import java.util.*;

public class S5_11815 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long N = sc.nextLong();
        
        for (int i = 0; i < N; i++) {
            long temp = sc.nextLong();

            long tempSqrt = (long)Math.floor(Math.sqrt((double)temp));

            if (tempSqrt * tempSqrt == temp)
                System.out.print(1);
            else
                System.out.print(0);
            
            if (i != N - 1)
                System.out.print(" ");
        }

        sc.close();
    }
}
