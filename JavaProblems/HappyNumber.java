package leetcode;

import java.util.Set;
import java.util.HashSet;

public class HappyNumber {
    public static boolean isHappy(int n) {

        Set<Integer> reachedNumbers = new HashSet<Integer>();

        while(reachedNumbers.add(n)){
            int digits = 0;

            while(n>0){
                digits += Math.pow(n % 10, 2);
                n /= 10;
            }

            n = digits;

            if (n==1){
                return true;
            }

        }

        return false;
    }

    public static void main(String [] args){
        int number = 19;
        System.out.println("Is Happy: "+isHappy(number));
    } 
}
    