/**
 * 
 */
package linkedList;

/**
 * @author mkakollu
 *
 */
public class ReverseLinkedList {

	public class Node {
		int data;
		Node next;

		public Node(int data) {
			this.data = data;
		}
	}
	
	public Node reverse(Node head) {
		Node pre = null;
		Node cur = head;
		while(cur != null) {
			Node next = cur.next;
			cur.next = pre;
			pre = cur;
			cur = next;
		}
		return pre;
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		ReverseLinkedList obj = new ReverseLinkedList();
		Node head = obj.new  Node(1);
		head.next = obj.new Node(2);
		head.next.next = obj.new Node(3);
		head.next.next.next = obj.new Node(4);
		head.next.next.next.next = obj.new Node(5);
		
		head = obj.reverse(head);
		while(head != null) {
			System.out.print(head.data + " ");
			head = head.next;
		}
		System.out.println();
		

	}

}
