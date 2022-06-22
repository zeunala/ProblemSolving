/*
한수

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

- N의 범위가 작으므로 1부터 차근차근 구해나가자.
* Pass/1st/00:10:23
*/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class S4_1065 {
    public static boolean checkHansu(int n) { // n이 한수인지 여부 리턴
        boolean result = true;
        List<Integer> numSplit = new ArrayList<Integer>();
        int gap;

        if (n <= 99) return true; // 두 자리 수 까지는 무조건 한 수이다.
        
        while (n > 0) {
            numSplit.add(n % 10);
            n /= 10;
        }

        gap = numSplit.get(1) - numSplit.get(0);
        
        for (int i = 0; i < numSplit.size() - 1; i++) {
            if (numSplit.get(i + 1) - numSplit.get(i) != gap) {
                result = false;
                break;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[] answer = new int[1001];
        Scanner sc = new Scanner(System.in);

        for (int i = 1; i <= 1000; i++) {
            if (checkHansu(i))
                answer[i] = 1;
            else
                answer[i] = 0;
            
            answer[i] += answer[i - 1];
        }
        
        System.out.println(answer[sc.nextInt()]);

        sc.close();
    }
}
