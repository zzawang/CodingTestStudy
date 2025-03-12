import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int[] arr;  // k의 원소들
    private static int N, K, answer;

    public static void find(int depth, int num) {
        if (depth == 8) return;

        num *= 10;

        if (num > N) return;

        for (int i = 0; i < K; i++) {
            int tmp = num + arr[i];
            if (tmp > N) continue;
            answer = Math.max(answer, tmp);
            find(depth + 1, tmp);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new int[K];
        st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < K; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        find(0, 0);
        System.out.println(answer);
    }
}