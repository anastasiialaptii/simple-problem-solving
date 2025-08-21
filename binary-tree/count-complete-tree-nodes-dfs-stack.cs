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
    public int CountNodes(TreeNode root) {
       if(root==null) return 0;

       var count = 0;
       var stack = new Stack<TreeNode>();
       stack.Push(root);

       while (stack.Count()>0) {
        var node = stack.Pop();

        if(node.left!=null) stack.Push(node.left);
        if(node.right!=null) stack.Push(node.right);

        count++;
       }
       
       return count;
    }
}