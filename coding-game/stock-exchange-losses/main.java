import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int nbValues = in.nextInt();

        int worstInvestment = 0;
        int currentHighest = 0;
        for (int i = 0; i < nbValues; i++) {
            int value = in.nextInt();
            currentHighest = Math.max(currentHighest,value);
            worstInvestment = Math.min(worstInvestment, value - currentHighest);
        }

        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");

        System.out.println(worstInvestment);
    }
}