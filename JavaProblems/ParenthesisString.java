package JavaProblems;

public class ParenthesisString {

    public static boolean checkValidString(String s){
        if (s.equals(""))
            return true;

        if (s.charAt(0)==')') 
            return false;

        int max_open = 0;
        int min_open = 0;

        for (int i=0; i<s.length(); i++){
            char c = s.charAt (i);

            min_open = c == '(' ? min_open + 1 :  min_open - 1;
            max_open = c != ')' ? max_open + 1 : max_open -1;

            if (max_open < 0)
                return false;

            min_open = min_open >= 0 ? min_open : 0;
        }

        return min_open == 0;
    }
    public static void main(String [] args){
        String paren="(*)";
        System.out.println("Is valid: "+checkValidString(paren));
    } 
}
    