import java.util.ArrayList;

class Solution {
    public String makeGood(String s) {
        for (int i = 0; i < s.length() - 1; i++) {
            if (Math.abs(s.charAt(i) - s.charAt(i + 1)) == 32) {
                s = s.substring(0, Math.max(0, i)) + s.substring(Math.min(s.length(),i+2));
                i = Math.max(-1, i - 2);
            }
        }

        return s;
    }
}