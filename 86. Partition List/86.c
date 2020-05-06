/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* partition(struct ListNode* head, int x){
    struct ListNode* head1 = NULL;
    struct ListNode* head2 = NULL;
    struct ListNode* tmp1 = NULL;
    struct ListNode* tmp2 = NULL;
    int flag1 = 0;
    int flag2 = 0;

    while(head != NULL){
        if(head->val < x){
            if(flag1 == 0){
                flag1 = 1;
                head1 = head;
                tmp1 = head;
            }else
            {
                tmp1->next = head;
                tmp1 = head;
            }
        }else{
            if(flag2 == 0){
                flag2 = 1;
                head2 = head;
                tmp2 = head;
            }else
            {
                tmp2->next = head;
                tmp2 = head;
            }
        }
        head = head->next;
    }

    if(head1 != NULL){
        tmp1->next = head2;
    }
    if(head2 != NULL){
        tmp2->next = NULL;
    }

    if(head1 != NULL){
        return head1;
    }
    return head2;
}

