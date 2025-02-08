class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummynode = new ListNode(-1);
        ListNode* curr = dummynode;

        ListNode* temp1 = l1;
        ListNode* temp2 = l2;

        int carry = 0;

        while (temp1 != nullptr || temp2 != nullptr) {
            int sum = carry;
            if (temp1) sum += temp1->val;
            if (temp2) sum += temp2->val;

            // Create a new node for the current digit of the result
            ListNode* newNode = new ListNode(sum % 10);
            carry = sum / 10; // Update carry for the next iteration
            curr->next = newNode;
            curr = curr->next;

            // Move to the next nodes in input lists if available
            if (temp1) temp1 = temp1->next;
            if (temp2) temp2 = temp2->next;
        }

        // If there's a remaining carry, create a new node for it
        if (carry) {
            ListNode* newNode = new ListNode(carry);
            curr->next = newNode;
        }

        return dummynode->next;
    }
};
