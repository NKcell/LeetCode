/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* getNode(TreeNode* root, int val){
        if(root == NULL){
            return NULL;
        }else if(root->val == val){
            return root;
        }else if(root->val>val){
            return getNode(root->left, val);
        }else{
            return getNode(root->right, val);
        }
    }
    
    TreeNode* searchBST(TreeNode* root, int val) {
        return this->getNode(root, val);
    }
};