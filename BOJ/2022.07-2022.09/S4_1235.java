/*
입력
첫째 줄에는 학생의 수 N(2≤N≤1,000)이 주어진다.
둘째 줄부터 N개의 줄에 걸쳐 각 학생의 학생 번호가 순서대로 주어진다.
모든 학생들의 학생 번호는 서로 다르지만 그 길이는 모두 같으며, 0부터 9 사이의 숫자로 이루어진 문자열이 주어진다.
문자열의 길이는 100보다 작거나 같다.

출력
첫째 줄에 구하고자 하는 가장 작은 k값을 출력한다.

- N과 문자열 길이가 크지 않으므로 k가 1인 경우부터 순서대로 체크한다.
* Fail/1st/00:10:01
*/
import java.util.*;

public class S4_1235 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];

        for (int i = 0; i < N; i++)
            arr[i] = sc.nextInt();
        
        for (int k = 1; ; k++) { // 입력 번호가 모두 다르므로 반드시 종료됨
            Set<Integer> tempMap = new HashSet<>();
            boolean isValid = true; // 입력 번호가 모두 다르면 true, 그렇지 않으면 false

            for (int e : arr) {
                if (tempMap.contains(e % (int)Math.pow(10, k))) {
                    isValid = false;
                    break;
                } else {
                    tempMap.add(e % (int)Math.pow(10, k));
                }
            }

            if (isValid) {
                System.out.println(k);
                break;
            }
        }

        sc.close();
    }
}
