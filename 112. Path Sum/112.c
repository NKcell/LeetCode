/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool hasPathSum(struct TreeNode* root, int sum){
    if (root == NULL){
        return 0;
    }

    sum -= root->val;

    if (sum == 0 && root->left == NULL && root->right==NULL){
        return 1;
    }

    return hasPathSum(root->left, sum) || hasPathSum(root->right, sum);
}