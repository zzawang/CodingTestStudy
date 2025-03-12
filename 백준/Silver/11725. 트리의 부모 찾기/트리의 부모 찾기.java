import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static int[] parents;
    private static boolean[] visited;
    private static List<Integer>[] connected;

    public static void dfs(int node) {
        visited[node] = true;

        for (int child : connected[node]) {
            if (!visited[child]) {
                parents[child] = node;
                dfs(child);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        parents = new int[N + 1];
        visited = new boolean[N + 1];
        connected = new ArrayList[N + 1];

        for (int i = 0; i <= N; i++) {
            connected[i] = new ArrayList<>();
        }

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            connected[n1].add(n2);
            connected[n2].add(n1);
        }

        dfs(1);

        for (int i = 2; i <= N; i++) {
            System.out.println(parents[i]);
        }
    }
}