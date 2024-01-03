import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    public String[] solution(String[] records) {
        ArrayList<String> answer = new ArrayList<>();
        HashMap<String, String> names = new HashMap<>();
        
        for (String record : records) {
            String[] prompt = record.split(" ");
            if (!prompt[0].equals("Leave")) {
                names.put(prompt[1], prompt[2]);
            }
        }
        
        for (String record : records) {
            String[] prompt = record.split(" ");
            if (prompt[0].equals("Enter")) {
                answer.add(names.get(prompt[1]) + "님이 들어왔습니다.");
            } else if (prompt[0].equals("Leave")) {
                answer.add(names.get(prompt[1]) + "님이 나갔습니다.");
            }
        }
        
        return answer.toArray(new String[0]);
    }
}