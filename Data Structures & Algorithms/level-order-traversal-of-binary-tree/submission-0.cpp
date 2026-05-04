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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> levels;
        dfs(root, 0, levels);
        return levels;
    }
    void dfs(TreeNode* node, int level, vector<vector<int>>& levels) {
        if (!node) return;
        if (level == levels.size()) {
            levels.push_back({});
        }
        levels[level].push_back(node->val);
        dfs(node->left, level + 1, levels);
        dfs(node->right, level + 1, levels);

    }
};
