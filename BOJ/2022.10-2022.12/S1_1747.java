/*
소수&팰린드롬

입력
첫째 줄에 N이 주어진다.

출력
첫째 줄에 조건을 만족하는 수를 출력한다.

- 소수 목록을 구해서 소수판단 기능을 만들고, 팰린드롬 판단 기능도 만들어 둘을 결합한다.
100만이상중 조건 만족하는 가장 작은 수는 1003001이므로 여기 범위까지만 체크하도록 한다.
* Pass/1st/00:26:13
*/
import java.util.*;
import java.util.stream.Collectors;

public class S1_1747 {
    public static boolean isReverseSame(int num) { // 팰린드롬 판단 여부 리턴
        String original = Integer.toString(num);
        for (int i = 0; i < original.length() / 2; i++) {
            if (original.charAt(i) != original.charAt(original.length() - 1 - i)) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        final int checkPrimeRange = 1005000;
        boolean[] isPrime = new boolean[checkPrimeRange];
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;

        for (int i = 2; i <= Math.floor(Math.sqrt(checkPrimeRange)); i++) {
            if (isPrime[i] == false) {
                continue;
            }

            int j = 2;
            while (i * j < isPrime.length) {
                isPrime[i * j] = false;
                j++;
            }
        }

        List<Integer> isPrimeSet = new ArrayList<>(); // 소수들만을 담은 리스트생성
        for (int i = 2; i < isPrime.length; i++) {
            if (isPrime[i]) {
                isPrimeSet.add(i);
            }
        }

        List<Integer> isPrimeAndReverseSame = isPrimeSet.stream()
                                                        .filter(num -> isReverseSame(num))
                                                        .filter(num -> num >= N)
                                                        .collect(Collectors.toList());
        System.out.println(isPrimeAndReverseSame.get(0));
        sc.close();
    }
}
