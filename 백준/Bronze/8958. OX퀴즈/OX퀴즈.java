import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = Integer.parseInt(scanner.nextLine());

        while (count-- > 0) {
            char[] testcase = scanner.nextLine().toCharArray();
            int answer = 0;
            int continuity = 1;

            for (int index = 0; index < testcase.length; index++) {
                if (testcase[index] == 'O') {
                    answer += continuity;
                    continuity += 1;
                } else {
                    continuity = 1;
                }
            }
            System.out.println(answer);
        }
    }
}
