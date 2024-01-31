import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] input = new int[8];

        for (int i = 0; i < 8; i++) {
            input[i] = scanner.nextInt();
        }

        if (isAscending(input)) {
            System.out.println("ascending");
        } else if (isDescending(input)) {
            System.out.println("descending");
        } else {
            System.out.println("mixed");
        }
    }

    static boolean isAscending(int[] array) {
        for (int i = 0; i < 8; i++) {
            if (array[i] != i + 1) {
                return false;
            }
        }
        return true;
    }

    static boolean isDescending(int[] array) {
        for (int i = 0; i < 8; i++) {
            if (array[i] != 8 - i) {
                return false;
            }
        }
        return true;
    }
}