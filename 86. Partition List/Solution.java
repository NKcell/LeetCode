/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode head1 = null;
        ListNode head2 = null;
        ListNode tmp1 = null;
        ListNode tmp2 = null;
        int flag1 = 0;
        int flag2 = 0;

        while (head != null){
            if (head.val < x){
                if (flag1 == 0){
                    flag1 = 1;
                    head1 = head;
                    tmp1 = head;
                }else{
                    tmp1.next = head;
                    tmp1 = head;
                }
            }else{
                if (flag2 == 0){
                    flag2 = 1;
                    head2 = head;
                    tmp2 = head;
                }else{
                    tmp2.next = head;
                    tmp2 = head;
                }
            }
            head = head.next;
        }

        if(head1 != null){
            tmp1.next = head2;
        }
        if(head2 != null){
            tmp2.next = null;
        }

        if(head1 != null){
            return head1;
        }
        return head2;
    }
}