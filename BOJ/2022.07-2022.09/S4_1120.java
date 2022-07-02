/*
문자열

입력
첫째 줄에 A와 B가 주어진다. A와 B의 길이는 최대 50이고, A의 길이는 B의 길이보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.

출력
A와 B의 길이가 같으면서, A와 B의 차이를 최소가 되도록 했을 때, 그 차이를 출력하시오.

- 길이의 범위가 작으므로 A를 한 칸씩 이동시키면서 차이들을 체크하고 그 최솟값을 출력하도록 한다.
* Pass/1st/00:09:01
*/
import java.util.*;

public class S4_1120 {
    public static int calcGap(String a, String b, int idx) { // a를 idx 칸 만큼 이동시키고 b와의 차이를 계산해 리턴한다.
        int result = 0;
        
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i + idx))
                result++;
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        String a = input[0];
        String b = input[1];

        int answer = 10000;

        for (int i = 0; i <= b.length() - a.length(); i++) {
            int temp = calcGap(a, b, i);

            if (answer > temp)
                answer = temp;
        }

        System.out.println(answer);

        sc.close();
    }
}
