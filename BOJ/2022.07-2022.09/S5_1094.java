/*
막대기

입력
첫째 줄에 X가 주어진다. X는 64보다 작거나 같은 자연수이다.

출력
문제의 과정을 거친다면, 몇 개의 막대를 풀로 붙여서 Xcm를 만들 수 있는지 출력한다.

- 문제의 과정을 정확하게 구현하면 되는 문제로 보인다.
* Pass/1st/00:15:39
*/
import java.util.*;

public class S5_1094 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> arr = new ArrayList<>(); // 막대들의 배열
        int remainLength = 64; // 남은 막대의 길이
        int targetLength = sc.nextInt();
        
        
        arr.add(64); // 처음 시작
        while (remainLength > targetLength) {
            // 막대를 하나 꺼내고
            int temp = arr.get(arr.size() - 1);
            arr.remove(arr.size() - 1);

            // 그 막대를 반으로 자른다.
            temp /= 2;

            // 막대 절반은 일단 배열에 넣고
            arr.add(temp);
            
            // 남은 막대 절반은 조건에 따라 버리거나 넣는다.
            if (remainLength - temp < targetLength)
                arr.add(temp);
            else
                remainLength -= temp;
        }

        System.out.println(arr.size());

        sc.close();
    }
}
