import java.util.*;

class Solution {
    private int max_length;
    private boolean[] visited;
    private Set<Integer> answer = new HashSet<>();
    private ArrayList<String> result = new ArrayList<>();
    
    public boolean isValid(int num) {
        int count = 0;
        
        if (num == 0 || num == 1) return false;
        
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
        
    public void dfs(int index, int depth, String numbers) {
        if (result.size() > 0) {
            int num = Integer.parseInt(String.join("", result));
            if (isValid(num)) {
                answer.add(num);
            }
        }
        
        if (depth == max_length) return;
        
        for (int i = 0; i < max_length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                result.add(String.valueOf(numbers.charAt(i)));
                dfs(i, depth + 1, numbers);
                visited[i] = false;
                result.remove(result.size() - 1);   
            }
        }
    }
    
    public int solution(String numbers) {
        max_length = numbers.length();
        visited = new boolean[max_length];
        dfs(0, 0, numbers);
        return answer.size();
    }
}