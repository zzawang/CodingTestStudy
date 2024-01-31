import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] s = scanner.nextLine().split(" ");
        String[] ascend = new String[]{"1", "2", "3", "4", "5", "6", "7", "8"};
        String[] descend = new String[]{"8", "7", "6", "5", "4", "3", "2", "1"};

        if (Arrays.equals(s, ascend)) {
            System.out.print("ascending");
        } else if (Arrays.equals(s, descend)) {
            System.out.print("descending");
        } else {
            System.out.print("mixed");
        }
    }
}