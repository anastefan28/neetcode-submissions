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
    vector<int> nodes;
    vector<int> rightSideView(TreeNode* root) {
        dfs(root,0);
        return nodes;
    }
    void dfs(TreeNode* node, int depth){
        if(!node) return;
        if (nodes.size() == depth) {
            nodes.push_back(node->val);
        }
        dfs(node->right, depth+1);
        dfs(node->left, depth+1);
    }
};
