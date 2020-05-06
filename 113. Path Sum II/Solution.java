import java.util.ArrayList;
import java.util.List;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}


class Solution {
    ArrayList<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        dfs(root, sum, new ArrayList<Integer>());
        return res;
    }

    private void dfs(TreeNode root, int sum, ArrayList<Integer> tmp){
        if(root == null){
            return;
        }

        sum -= root.val;
        tmp.add(root.val);

        if(sum == 0 && root.left == null && root.right == null){
            res.add(tmp);
            return;
        }

        dfs(root.left, sum, new ArrayList<>(tmp));
        dfs(root.right, sum, new ArrayList<>(tmp));
    }
}