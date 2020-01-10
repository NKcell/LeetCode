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


int getDecimalValue(struct ListNode* head){
    int tmp = 0;
    
    while(head!=NULL){
        tmp = (tmp<<1) + head->val;
        head = head->next;
    }
    return tmp;
}
