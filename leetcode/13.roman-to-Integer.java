import java.util.*;
import java.util.HashMap;

class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> L = new HashMap<>();
        L.put('I', 1);
        L.put('V', 5);
        L.put('X', 10);
        L.put('L', 50);
        L.put('C', 100);
        L.put('D', 500);
        L.put('M', 1000);

        int total = 0;
        int previous = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            int current = L.get(s.charAt(i));
            
            if (current < previous) {
                total -= current;
            } else {
                total += current;
                previous = current;
            }
        }
        
        return total;
    }
}
