import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static boolean[][] incompatible;
    // N은 아이스크림 종류의 수이고, M은 섞어먹으면 안 되는 조합의 개수
    private static int N, M, answer = 0;

    public static boolean isValid(int[] selected) {
        return !(incompatible[selected[0]][selected[1]] ||
                incompatible[selected[1]][selected[0]] ||
                incompatible[selected[0]][selected[2]] ||
                incompatible[selected[2]][selected[0]] ||
                incompatible[selected[1]][selected[2]] ||
                incompatible[selected[2]][selected[1]]);
    }

    public static void find(int num, int depth, int[] selected) {
        if (depth == 3) {
            if (isValid(selected)) {
                answer++;
            }
            return;
        }

        for (int i = num; i < N; i++) {
            selected[depth] = i;
            find(i + 1, depth + 1, selected);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        incompatible = new boolean[N][N];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int ice1 = Integer.parseInt(st.nextToken()) - 1;
            int ice2 = Integer.parseInt(st.nextToken()) - 1;
            incompatible[ice1][ice2] = true;
            incompatible[ice2][ice1] = true;
        }

        int[] selected = new int[3];
        find(0, 0, selected);
        System.out.println(answer);
    }
}