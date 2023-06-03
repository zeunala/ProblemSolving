/*
타일 위의 대각선

입력
첫째 줄에 가로의 길이 xcm와 세로의 길이 ycm가 주어진다.
x와 y는 1,000,000,000 이하의 자연수이다.
x와 y사이에는 빈칸이 하나 이상 있다.

출력
첫째 줄에 대각선이 그려져 있는 타일의 개수를 출력한다.

- x와 y의 최대공약수를 a라고 하면 (x/a) * (y/a)의 직사각형 a개로 나눌 수 있다. (x/a와 y/a는 서로소)
이때 각 직사각형에는 대각선이 x/a + y/a - 1개 그어져 있다.
* Fail/1st/00:12:37/RuntimeError
*/
import java.util.*;

public class S1_2168 {
    public static int gcd(int a, int b) {
        if (a < b) {
            return gcd(b, a);
        }

        if (a % b == 0) {
            return b;
        }

        return gcd(a - b, b);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        int gcdAB = gcd(a, b);

        System.out.println(gcdAB * ((a / gcdAB) + (b / gcdAB) - 1));
        
        sc.close();
    }
}
