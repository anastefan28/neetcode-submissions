/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<int> arr;
    int kthSmallest(TreeNode* root, int k) {
        srd(root,arr);
        return arr[k-1];
    }
    void srd(TreeNode* node, vector<int>& arr){
        if(!node) return;
        srd(node->left, arr);
        arr.push_back(node->val);
        srd(node->right,arr);
    }

};
