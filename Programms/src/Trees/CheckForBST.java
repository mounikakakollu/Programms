package Trees;

import Trees.LevelOrderTraversaOfBST.Node;

/**Determine if the binary tree is a binary search tree
* Given a Binary Tree, figure out whether it's a Binary Search Tree. In a binary search tree, 
* each node's key value is smaller than the key value of all nodes in the right subtree, 
* and are greater than the key values of all nodes in the left subtree i.e. L < N < R.
 * @author mounika
 *
 */
public class CheckForBST {
	
	public boolean checkForBST(Node ptr) {
		boolean status;
		if(ptr == null)
			return true;
		else {
			if(ptr.left != null && ptr.left.data > ptr.data)
				return false;
			else if(ptr.right != null && ptr.right.data < ptr.data) 
				return false;
			status = checkForBST(ptr.left);
			status = checkForBST(ptr.right);
			return status;
		}
	}
	
	public static void main(String[] args) {
		LevelOrderTraversaOfBST obj = new LevelOrderTraversaOfBST();
		Node head = obj.new Node(100);
		head.left = obj.new Node(50);
		head.right = obj.new Node(200);
		head.left.left = obj.new Node(25);
		head.left.right = obj.new Node(75);
		head.right.right = obj.new Node(300);
		head.right.right.right =  obj.new Node(350);
		CheckForBST obj1 = new CheckForBST();
		System.out.println(obj1.checkForBST(head));
		
	}

}
