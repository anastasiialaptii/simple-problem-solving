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
    public IList<string> BinaryTreePaths(TreeNode root) {
        var result = new List<string>();
        var stack = new Stack<(TreeNode node, string path)>();

        stack.Push((root, root.val.ToString()));

        while(stack.Count > 0) {
            var (node, path) = stack.Pop();

            if(node.left == null && node.right == null) {
                result.Add(path);
            }

            if(node.left !=null) {
                stack.Push((node.left, path + "->" + node.left.val));
            }

            if(node.right !=null) {
                stack.Push((node.right, path + "->" + node.right.val));
            }
        }

        return result;
    }
}