class Solution {


    public boolean isPalindrome(int x) {
        
        int newX = 0;
        int temp = x;
        while (temp != 0) {
            newX = (newX * 10) + temp % 10;
            temp /= 10;
        }   
        System.out.println(newX);
        return newX == x;
    }


    public boolean isPalindrome1(int x) {
        String text = String.valueOf(x);
        for (int i = 0; i < text.length() / 2; i++) {
            if (text.charAt(i) == text.charAt(text.length() - i)) {
                return false;
            }
        }
        return true;
    }
}