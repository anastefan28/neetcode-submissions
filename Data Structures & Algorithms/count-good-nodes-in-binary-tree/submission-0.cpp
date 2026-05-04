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
    int good=0;

    int goodNodes(TreeNode* root) {
        dfs(root, root->val);
        return good;
    }
    void dfs(TreeNode* node, int pathMax){
        if(!node) return;
        if(node->val>=pathMax){
            pathMax=node->val;
            good++;
        }
        dfs(node->left, pathMax);
        dfs(node->right, pathMax);
    }

};
