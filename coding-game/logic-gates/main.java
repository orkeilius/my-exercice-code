import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {

        HashMap<String,String> map = new HashMap<String,String>();

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        for (int i = 0; i < n; i++) {
            String inputName = in.next();
            String inputSignal = in.next();
            map.put(inputName, inputSignal);
        }
        for (int i = 0; i < m; i++) {
            String outputName = in.next();
            String type = in.next();
            String inputName1 = in.next();
            String inputName2 = in.next();

            String newSignal = "";
            for (int j = 0; j < map.get(inputName1).length(); j++) {
                boolean x = map.get(inputName1).charAt(j) == '-';
                boolean y = map.get(inputName2).charAt(j) == '-';
                switch(type){
                    case "AND":
                        newSignal += x && y ? "-" : "_";
                        break;
                    case "OR":
                        newSignal += x || y ? "-" : "_";
                        break;
                    case "XOR":
                        newSignal += ( x || y ) && ! ( x && y ) ? "-" : "_";
                        break;
                    case "NAND":
                        newSignal += !(x && y) ? "-" : "_";
                        break;
                    case "NOR":
                        newSignal += !(x || y) ? "-" : "_";
                        break;
                    case "NXOR":
                        newSignal += !(( x || y ) && ! ( x && y )) ? "-" : "_";
                        break;
                }
            }
            System.out.printf("%s %s\n",outputName,newSignal);
        }
    }
}