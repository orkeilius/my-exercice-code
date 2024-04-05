import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    private static HashMap<String, Integer> values = new HashMap<String, Integer>();


    public static void main(String args[]) {
        
        values.put("A", 14);
        values.put("2", 2);
        values.put("3", 3);
        values.put("4", 4);
        values.put("5", 5);
        values.put("6", 6);
        values.put("7", 7);
        values.put("8", 8);
        values.put("9", 9);
        values.put("10", 10);
        values.put("J", 11);
        values.put("Q", 12);
        values.put("K", 13);


        Scanner in = new Scanner(System.in);


        int nbCard1 = in.nextInt(); // the number of cards for player 1
        Queue<Integer> file1 = new LinkedList<Integer>();
        for (int i = 0; i < nbCard1; i++) {
            String cardp1 = in.next(); // the n cards of player 1
            file1.offer(values.get(cardp1.substring(0, cardp1.length() - 1)));
        }
        int nbCard2 = in.nextInt(); // the number of cards for player 1
        Queue<Integer> file2 = new LinkedList<Integer>();
        for (int i = 0; i < nbCard2; i++) {
            String cardp2 = in.next(); // the n cards of player 1
            file2.offer(values.get(cardp2.substring(0, cardp2.length() - 1)));
        }
         
        Queue<Integer> pile1 = new LinkedList<Integer>();
        Queue<Integer> pile2 = new LinkedList<Integer>();
        int nbManche = 0;
        boolean bataille = false;
        // gameloop
        while(!file1.isEmpty() && !file2.isEmpty()){
            if (!bataille){
                nbManche++;
            }
            
            int elem1 = file1.peek();
            pile1.offer(file1.poll());
            int elem2 = file2.peek();
            pile2.offer(file2.poll());

            if (elem1 < elem2){
                while(!pile1.isEmpty()){
                    file2.offer(pile1.poll());
                }
                while(!pile2.isEmpty()){
                    file2.offer(pile2.poll());
                }
                bataille = false;
            }
            else if (elem2 < elem1){
                while(!pile1.isEmpty()){
                    file1.offer(pile1.poll());
                }
                while(!pile2.isEmpty()){
                    file1.offer(pile2.poll());
                }
                bataille = false;
            }
            else {
                bataille = true;
                if(file1.size() < 3 || file2.size() < 3){
                    break;
                }
                for (int i = 0; i < 3; i++) {
                    pile1.offer(file1.poll()); 
                    pile2.offer(file2.poll()); 
                }
            }
        }

        if (bataille){
            System.out.printf("PAT");
        } else if (file1.isEmpty()){
            System.out.printf("2 %s",nbManche);
        } else {
            System.out.printf("1 %s",nbManche);
        }
    }
}