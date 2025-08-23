/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {

    public int CheckHeight(TreeNode node) {
        if(node == null) return 0;

        var left = CheckHeight(node.left);
        
        if (left == -1) return -1;

        var right = CheckHeight(node.right);
        
        if (right == -1) return -1;

        if (Math.Abs(left - right) > 1) return -1; 

        return 1 + Math.Max(left, right);
    }
    public bool IsBalanced(TreeNode root) {        
        if(CheckHeight(root) == -1) return false;

        return true;
    }
}