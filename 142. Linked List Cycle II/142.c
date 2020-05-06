/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *detectCycle(struct ListNode *head) {
    struct ListNode* fast = head;
    struct ListNode* slow = head;
    int flag = 0;

    while(fast != NULL && fast->next != NULL){
        fast = fast->next->next;
        slow = slow->next;

        if (fast == slow){
            flag = 1;
            break;
        }
    }

    if (flag == 0){
        return NULL;
    }

    while(head != slow){
        head = head->next;
        slow = slow->next;
    }

    return head;
}