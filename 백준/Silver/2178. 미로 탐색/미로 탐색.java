import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    private static int N, M, answer = 0;
    private static char[][] arr;
    private static boolean[][] visited;

    public static class Point {
        public int x, y, sum;
        public Point(int x, int y, int sum) {
            this.x = x;
            this.y = y;
            this.sum = sum;
        }
    }


    public static void bfs(int startX, int startY) {
        Integer[] dx = {0, 0, -1, 1};
        Integer[] dy = {-1, 1, 0, 0};

        Queue<Point> queue = new LinkedList<>();

        queue.add(new Point(startX, startY, 1));
        visited[startX][startY] = true;

        while(!queue.isEmpty()) {
            Point point = queue.poll();
            int x = point.x;
            int y = point.y;
            int sum = point.sum;

            if (x == N - 1 && y == M - 1) {
                answer = sum;
                return;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && 0 <= ny && nx < N && ny < M && !visited[nx][ny] && arr[nx][ny] == '1') {
                    visited[nx][ny] = true;
                    queue.add(new Point(nx, ny, sum + 1));
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        visited = new boolean[N][M];
        arr = new char[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = st.nextToken().toCharArray();
        }

        bfs(0, 0);
        System.out.println(answer);
    }
}