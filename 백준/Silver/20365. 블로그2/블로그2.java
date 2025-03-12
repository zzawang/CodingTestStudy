import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        char[] arr = br.readLine().toCharArray();

        Map<String, Integer> counter = new HashMap<>();
        counter.put("B", 0);
        counter.put("R", 0);

        int start = 0;
        int end;
        for (int i = 1; i < N; i++) {
            end = i;
            if (arr[start] != arr[end]) {
                int tmp = counter.get(String.valueOf(arr[start]));
                counter.put(String.valueOf(arr[start]), tmp + 1);
                start = end;
            }
        }

        System.out.println(Math.max(counter.get("B"), counter.get("R")) + 1);
    }
}