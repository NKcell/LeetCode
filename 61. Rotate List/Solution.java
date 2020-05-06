/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        int linkLen = 1;
        ListNode tmpHead = head;
        if (tmpHead == null || tmpHead.next == null){
            return head;
        }

        while (tmpHead.next != null){
            linkLen ++;
            tmpHead = tmpHead.next;
        }

        k = k%linkLen;
        int pre = linkLen-k-1;
        if (pre == -1){
            return head;
        }

        ListNode tmpHead2 = head;
        int tmp = 0;
        while(tmp != pre){
            tmp ++;
            tmpHead2 = tmpHead2.next;
        }

        tmpHead.next = head;
        head = tmpHead2.next;
        tmpHead2.next = null;

        return head;
    }
}