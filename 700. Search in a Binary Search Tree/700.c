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

struct TreeNode* getNode(struct TreeNode* root, int val){
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

struct TreeNode* searchBST(struct TreeNode* root, int val){
    return getNode(root, val);
}


