/**
 * 
 */
package Trees;

import Trees.LevelOrderTraversaOfBST.Node;

/**Convert Binary Tree to it's mirror form
 * @author mkakollu
 *
 */
public class MirrorBinaryTree {

	public Node mirror(Node head) {
		if(head == null) 
			return null;
		Node left = mirror(head.left);
		Node right = mirror(head.right);
		head.left = right;
		head.right = left;
		return head;
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		LevelOrderTraversaOfBST node= new LevelOrderTraversaOfBST();		
		Node head = node.new Node(100);
		head.left = node.new Node(50);
		head.right = node.new Node(200);
		head.left.left = node.new Node(25);
		head.left.right = node.new Node(75);
		head.right.right = node.new Node(300);
		head.right.right.right =  node.new Node(350);
		node.inOrderTraversal(head);
		MirrorBinaryTree obj = new MirrorBinaryTree();
		head = obj.mirror(head);
		System.out.println();
		System.out.println("Mirror Tree");
		node.inOrderTraversal(head);

	}

}
