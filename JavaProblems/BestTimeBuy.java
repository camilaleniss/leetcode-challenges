package JavaProblems;

import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class BestTimeBuy{

    public static int INDICATOR = -1000000;

    public static int maxProfit( int[] prices){

        if (prices.length == 0){
            return 0;
        }

        Map<Integer[], ArrayList<Integer>> transactions = getPosibleTransactions(prices);

        int profit = calculateProfit(transactions);
        
        return profit;
    }

    public static Map<Integer[], ArrayList<Integer>> getPosibleTransactions(int[] prices){
        
        Map<Integer[], ArrayList<Integer>> transactions = new HashMap<>();

        Integer[] previous_price = {prices[0], 0};

        transactions.put(previous_price, new ArrayList<>());

        for (int i=1; i<prices.length; i++){
            ArrayList<Integer> previous_list = transactions.get(previous_price);
            int last = getLast(previous_list);

            if (last==INDICATOR && prices[i]<previous_price[0]){
                previous_price = new Integer[]{prices[i], i};
                transactions.put(previous_price, new ArrayList<>());

            }else if (last!=INDICATOR && last>prices[i]){
                previous_price = new Integer[]{prices[i], i};
                transactions.put(previous_price, new ArrayList<>());

            }else{
                previous_list.add(prices[i]);
                transactions.put(previous_price, previous_list);
            }
        }
        
        return transactions;
    }

    public static int calculateProfit(Map<Integer[], ArrayList<Integer>> transactions){
        int profit = 0;

        for (Integer[] key : transactions.keySet()) {
            ArrayList<Integer> list = transactions.get(key);
            if (list.size()!=0){
                profit += (list.get(list.size()-1) - key[0]);
            }
        }

        return profit;
    }

    public static int getLast(ArrayList<Integer> list){
        if(list!=null){
            if (list.size()!=0)
                return list.get(list.size()-1);
            
            return INDICATOR;
        }
        return INDICATOR;
    }

    public static void main( String[] args) {
        int[] prices =  {7,1,5,3,6,4};
        System.out.println(maxProfit(prices));
    } 
}