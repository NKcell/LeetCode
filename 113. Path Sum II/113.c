/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** pathSum(struct TreeNode* root, int sum, int* returnSize, int** returnColumnSizes){
    *returnSize = 0;
    *returnColumnSizes = (int*)malloc(0*sizeof(int));
    if(root==NULL){
        return NULL;
    }
    int tmpLen = 0;
    
    int** res = (int**)malloc(0*sizeof(int*));
    int** tmp = (int**)malloc(0*sizeof(int*));
    
    dfs(root, &res, returnSize, returnColumnSizes, sum, tmpLen, tmp);
    free(tmp);
    
    return res;
}

void dfs(struct TreeNode* root, int*** res, int* returnSize, int** returnColumnSizes, int sum, int tmpLen, int* tmp){
    if (root == NULL){
        return;
    }
    
    sum -= root->val;
    int* newtmp = (int*)malloc((tmpLen+1)*sizeof(int));
    memcpy(newtmp, tmp, tmpLen*sizeof(int));
    *(newtmp+tmpLen) = root->val;
    tmpLen++;
    
    if (sum==0 && root->left==NULL && root->right==NULL){
        *returnSize += 1;

        int* newreturnColumnSizes = malloc(*returnSize * sizeof(int));
        memcpy(newreturnColumnSizes, *returnColumnSizes, (*returnSize-1)*sizeof(int));
        *(newreturnColumnSizes+ *returnSize -1) = tmpLen;
        *returnColumnSizes = newreturnColumnSizes;
        

        int** newres = (int**)malloc(*returnSize*sizeof(int*));
        memcpy(newres, *res, (*returnSize-1)*sizeof(int*));
        *(newres+*returnSize-1) = newtmp;

        *res = newres;
        return;
    }

    dfs(root->left, res, returnSize, returnColumnSizes, sum, tmpLen, newtmp);   
    dfs(root->right, res, returnSize, returnColumnSizes, sum, tmpLen, newtmp);
    free(newtmp);
}