/*
물통

입력
첫째 줄에 세 정수 A, B, C가 주어진다.

출력
첫째 줄에 공백으로 구분하여 답을 출력한다.
각 용량은 오름차순으로 정렬한다.

- A와 C의 차이(A<=B<=C), B와 C의 차이(B<=C), A(C-A<=B), B(C-B<=A), C 다섯 경우가 가능하다.
* Fail/1st/00:16:55
- A, B가 그대로 가능한 경우는 각각 A<=C, B<=C 역시 추가로 만족해야 가능하고, 또한 B>=C인 경우 0도 가능하다. 
* Fail/2nd/00:21:37
- 2 4 3의 경우 0 0 3 -> 2 0 1 -> 0 2 1 과 같이 되므로 A와 C의 차이는 A<=B, A<=C일 때 가능하다.
* Fail/3rd/00:28:22
*/
import java.util.*;

public class G5_2251 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Set<Integer> allCase = new HashSet<>();

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        
        if (A <= B && A <= C) {
            allCase.add(C - A);
        }
        if (B <= C) {
            allCase.add(C - B);
        }
        if (C - A <= B && A <= C) {
            allCase.add(A);
        }
        if (C - B <= A && B <= C) {
            allCase.add(B);
        }
        allCase.add(C);
        if (B >= C) {
            allCase.add(0);
        }

        List<Integer> sortedCase = new ArrayList<>(allCase);
        Collections.sort(sortedCase);

        for (Integer e : sortedCase) {
            System.out.print(e + " ");
        }

        sc.close();
    }
}
