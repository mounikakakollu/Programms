/**
 * 
 */
package Trees;

import java.util.LinkedList;
import java.util.Queue;

/**Connect all siblings
 * Given the root to a binary tree where each node has an additional pointer called sibling (or next), 
 * connect the sibling pointer to the next node in the same level.
 * @author mounika
 *
 */
public class LevelOrderTraversaOfBST {
	
	public class Node {
		int data;
		Node left;
		Node right;
		Node next;
		
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
	
	public void inOrderTraversal(Node ptr) {
		if(ptr != null) {
			inOrderTraversal(ptr.left);
			System.out.print(ptr.data + " ");
			inOrderTraversal(ptr.right);
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
			tmp.next = queue.peek();
		}
		
	}
	
	public void assignNextPointer(Node ptr) {
		Queue<Node> queue = new LinkedList<Node>();
		queue.add(ptr);
		while(!queue.isEmpty()) {
			Node tmp = queue.poll();
			if (tmp.left !=null) {
				queue.add(tmp.left);
			}
			if (tmp.right != null) {
				queue.add(tmp.right);
			}
			tmp.next = queue.peek();
		}
		
		while(ptr != null) {
			System.out.print(ptr.data +" ");
			ptr = ptr.next;
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
		System.out.println("In Order traversal of BST");
		obj.inOrderTraversal(head);
		
		System.out.println();
		System.out.println("PostOrder traversal of BST");
		obj.PostOrderTraversal(head);
		
		System.out.println();
		System.out.println("Level Order traversal of BST");
		obj.LevelOrderTraversal(head);
		
		System.out.println();
		System.out.println("assignNextPointer");
		obj.assignNextPointer(head);
		
		// TODO Auto-generated method stub

	}

}
