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
    public int[] FindMode(TreeNode root) {
        if (root == null) return Array.Empty<int>();

        var stack = new Stack<TreeNode>();
        var arr = new List<int>();
        var dict = new Dictionary<int,int>();

        stack.Push(root);

        while(stack.Count>0) {
            var node = stack.Pop();

            if (dict.ContainsKey(node.val))
                {
                    dict[node.val]++;
                }
            else
            {
                dict.Add(node.val, 1);
            }

            if(node.left!=null) {
                stack.Push(node.left);
            }

            if(node.right!=null){
                stack.Push(node.right);
            }
        }
        
        var max = dict.Values.Max();

        foreach (var item in dict)
            if (item.Value == max) arr.Add(item.Key);

        return arr.ToArray();
    }
}