/**
 * 
 */
package Trees;

import java.util.LinkedList;
import java.util.Queue;

/**
 * @author mounika
 *
 */
public class LevelOrderTraversaOfBST {
	
	public class Node {
		int data;
		Node left;
		Node right;
		
		public Node(int data) {
			this.data = data;
		}
		
	}
	
	public void preOrderTraversal(Node ptr) {
		if(ptr != null) {
			System.out.print(ptr.data + " ");
			preOrderTraversal(ptr.left);
			preOrderTraversal(ptr.right);
		}
	}
	
	public void PostOrderTraversal(Node ptr) {
		if(ptr != null) {
			PostOrderTraversal(ptr.left);
			PostOrderTraversal(ptr.right);
			System.out.print(ptr.data + " ");
		}
	}
	
	public void LevelOrderTraversal(Node ptr) {
		Queue<Node> queue = new LinkedList<Node>();
		queue.add(ptr);
		while(!queue.isEmpty()) {
			Node tmp = queue.poll();
			System.out.print(tmp.data + " ");
			if (tmp.left !=null) {
				queue.add(tmp.left);
			}
			if (tmp.right != null) {
				queue.add(tmp.right);
			}
		}
		
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		LevelOrderTraversaOfBST obj = new LevelOrderTraversaOfBST();
		Node head = obj.new Node(100);
		head.left = obj.new Node(50);
		head.right = obj.new Node(200);
		head.left.left = obj.new Node(25);
		head.left.right = obj.new Node(75);
		head.right.right = obj.new Node(300);
		head.right.right.right =  obj.new Node(350);
		
		System.out.println("PreOrder traversal of BST");
		obj.preOrderTraversal(head);
		
		System.out.println();
		System.out.println("PostOrder traversal of BST");
		obj.PostOrderTraversal(head);
		
		System.out.println();
		System.out.println("Level Order traversal of BST");
		obj.LevelOrderTraversal(head);
		
		// TODO Auto-generated method stub

	}

}
