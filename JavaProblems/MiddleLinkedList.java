package JavaProblems; 

import java.util.ArrayList;

public class MiddleLinkedList {

    public static ListNode middleNode(ListNode head) {
        
        ArrayList<ListNode> listaconvertida = ConvertList(head, new ArrayList<ListNode>());

        int index_middle = listaconvertida.size()/2;

        return listaconvertida.get(index_middle);
    }

    public static ArrayList<ListNode> ConvertList(ListNode node, ArrayList<ListNode> array){
        if (node == null)
            return array;

        array.add(node);
        return ConvertList(node.next, array);
    }

    public static void main(String [] args){
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);   
        head.next.next.next.next = new ListNode(5);  
        head.next.next.next.next.next = new ListNode(6);      

        System.out.println(""+middleNode(head).val);

    }
}
