/*
기타줄

입력
첫째 줄에 N과 M이 주어진다.
N은 100보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다.
둘째 줄부터 M개의 줄에는 각 브랜드의 패키지 가격과 낱개의 가격이 공백으로 구분하여 주어진다.
가격은 0보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫째 줄에 기타줄을 적어도 N개 사기 위해 필요한 돈의 최솟값을 출력한다.

- N을 N/6*6과 N%6으로 나누고 그리디 알고리즘으로 각각에 대한 돈의 최솟값을 구해보도록 한다.
* Pass/1st/00:12:01
*/
import java.util.*;

public class S4_1049 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int priceOf6 = 100000; // 기타줄 6개의 최솟값
        int priceOf1 = 100000; // 기타줄 1개의 최솟값

        int answer = 0;
        
        for (int i = 0; i < M; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            if (priceOf6 > a)
                priceOf6 = a;
            if (priceOf1 > b)
                priceOf1 = b;
        }
        
        // 단품으로 사는게 더 싼 경우
        if (priceOf6 > priceOf1 * 6)
            priceOf6 = priceOf1 * 6;
        
        answer += (N / 6) * priceOf6;
        answer += Math.min((N % 6) * priceOf1, priceOf6); // N % 6개를 단품으로 사는 것보다 6개짜리를 사는게 더 쌀 수도 있다.

        System.out.println(answer);

        sc.close();
    }
}
