/*
셀프 넘버

입력
입력은 없다.

출력
10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.

- d(n) >= n이므로 n을 1부터 10000까지 루프 돌리면서 d(n)들을 체크하면 된다.
* Fail/1st/00:13:28
- 오타를 수정하였다.
* Pass/2nd/00:14:14
*/
public class S5_4673 {
    public static int calcD(int n) { // 입력 n에 대해 d(n)을 리턴한다.
        int result = n;
        int temp = result;

        while (temp > 0) {
            result += (temp % 10);
            temp /= 10;
        }

        return result;
    }

    public static void main(String[] args) {
        boolean[] arr = new boolean[10001]; // arr[n]은 n이 셀프 넘버인지 유무를 나타냄

        // 배열 초기화
        for (int i = 0; i <= 10000; i++) {
            arr[i] = true;
        }

        // 셀프 넘버 확인
        for (int i = 1; i <= 10000; i++) {
            int temp = calcD(i);
            if (temp <= 10000)
                arr[temp] = false;
        }

        // 결과 출력
        for (int i = 1; i <= 10000; i++) {
            if (arr[i])
                System.out.println(i);
        }
    }
}
