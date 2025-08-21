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

        var counter = 0;
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        while(queue.Count()>0) {
            var node = queue.Dequeue();

            if(node.left != null) queue.Enqueue(node.left);
            if(node.right != null) queue.Enqueue(node.right);
            
            counter++;
        }

        return counter;
    }
}