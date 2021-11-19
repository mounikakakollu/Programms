/**
 * 
 */
package Trees;
import Trees.LevelOrderTraversaOfBST.Node;;

/**Check if a given Binary Tree is SumTree
 * Write a function that returns true if the given Binary Tree is SumTree else false. 
 * A SumTree is a Binary Tree where the value of a node is equal to the sum of the nodes present in 
 * its left subtree and right subtree. An empty tree is SumTree and the sum of an empty tree can be considered as 0.
 *  A leaf node is also considered as SumTree.
 * @author mkakollu
 *
 */
public class CheckIfBstIsSumTree {
	
	public int sum(Node node) {
		if(node == null)
			return 0;
		return sum(node.left) + node.data + sum(node.right);
	}

	public boolean isSumTree(Node head) {
		CheckIfBstIsSumTree obj = new CheckIfBstIsSumTree();
		int ls = 0;
		int rs = 0;
		if(head == null || (head.left == null && head.right == null))
			return true;
		if(head.left == null)
			ls= 0;
		else if( head.left.left == null && head.left.right == null) {
			ls = head.left.data;
		}
		else {
			ls= 2*head.left.data;
		}
		
		if(head.right == null)
			rs= 0;
		else if( head.right.left == null && head.right.right == null) {
			rs = head.right.data;
		}
		else {
			rs= 2*head.right.data;
		}
		
		if(head.data == ls+rs && (isSumTree(head.left) && (isSumTree(head.right))))
			return true;
		else {
			return false;
		}
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		LevelOrderTraversaOfBST node= new LevelOrderTraversaOfBST();		
		CheckIfBstIsSumTree obj = new CheckIfBstIsSumTree();
		Node head = node.new Node(26);
		head.left = node.new Node(10);
		head.right = node.new Node(3);
		head.left.left = node.new Node(4);
		head.left.right = node.new Node(6);
		head.right.right = node.new Node(3);
//		head.right.right.right =  node.new Node(350);
		System.out.println(obj.isSumTree(head));
		

	}

}
