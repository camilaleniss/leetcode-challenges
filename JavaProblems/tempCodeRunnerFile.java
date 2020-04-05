package javaproblems;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Map;

public class BestTimeBuy{

    public static int maxProfit( int[] prices){

        Map<Integer, ArrayList<Integer>> transactions = getPosibleTransactions(prices);

        int profit = calculateProfit(transactions);
        
        return profit;
    }

    public static Map<Integer, ArrayList<Integer>> getPosibleTransactions(int[] prices){
        Map<Integer, ArrayList<Integer>> transactions = new HashMap<>();

        previous_price = prices[0];

        transactions.put(previous_price, new ArrayList<>());

        for (int i = 1; i<prices.lenght; i++){

            if (prices[i]<previous_price){
                previous_price = prices[i];
                transactions.put(previous_price, new ArrayList<>());
            }else{
                ArrayList<Integer> previous_list = transactions.get(previous_price).add(prices[i]);
                transactions.put(previous_price, previous_list);
            }

        }

        return transactions;
    }

    public static int calculateProfit(Map<Integer, ArrayList<Integer>> transactions){
        int profit = 0;

        for (Integer key : transactions.keySet()) {
            ArrayList<Integer> list = transactions.get(key);
            if (list.size()!=0){
                profit += (list.get(list.length-1) - key);
            }
        }

        return profit;
    }

    public static void main( String[] args) {
        int[] prices =  {7,1,5,3,6,4};
        System.out.println(maxProfit(prices));
    } 
}