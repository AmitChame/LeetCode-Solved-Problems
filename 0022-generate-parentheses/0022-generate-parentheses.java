class Solution {
    public List<String> generateParenthesis(int n) {
        
        List<String> answer = new ArrayList<>();
        
        generate("", 0, 0, n, answer);
        
        return answer;
    }
    
    private void generate(String current, int open, int close, int n, List<String> answer) {
        
        // If we used all n pairs
        if (current.length() == 2 * n) {
            answer.add(current);
            return;
        }
        
        // We can add '(' if we still have some left
        if (open < n) {
            generate(current + "(", open + 1, close, n, answer);
        }
        
        // We can add ')' only if there is an unmatched '('
        if (close < open) {
            generate(current + ")", open, close + 1, n, answer);
        }
    }
}