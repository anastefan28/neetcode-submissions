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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* current = head;
        int size = 0;
        while (current)
        {
            size++;
            current = current->next;
        }
        n = size - n;
        ListNode* prev = nullptr;
        current = head;
        int cnt = 0;
        while (current) {
            if (cnt == n) {
                if (prev) {
                    prev->next = current->next;
                    delete current;
                }
                else head = current->next;
                return head;
            }
            cnt++;
            prev = current;
            current = current->next;
        }
    }
};
