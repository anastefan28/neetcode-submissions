/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* l1current = l1;
        ListNode* l2current = l2;
        ListNode* sumList = nullptr;
        ListNode* prev = nullptr;
        int rest = 0;
        while (l1current || l2current) {
            int sum = 0;
            if (l1current) 
            {
                sum += l1current->val;
                l1current=l1current->next;
            }
            if (l2current) {
                sum += l2current->val;
                l2current=l2current->next;
            }
            sum += rest;
            rest = sum / 10;
            ListNode* newNode = new ListNode(sum % 10);

        if (!sumList) {
            sumList = newNode;
            prev = newNode;   
        }
        else {
            prev->next = newNode;
            prev = newNode;
        }
    }
    if (rest) {
        ListNode* newNode = new ListNode(rest);
        prev->next = newNode;
        prev = newNode;
    }
    return sumList;
    }
};
