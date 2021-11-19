package linkedList;

import linkedList.ReverseLinkedList.Node;

public class Seggregate012 {
	
	public Node seggregation(Node head, int ele) {
		Node pre = null;
		Node cur = head;
		while(cur != null) {
			if(cur.data == ele && pre != null) {
				Node next = cur.next;
				pre.next = next;
				cur.next = head;
				head = cur;
				cur = next;
			}
			else {
				pre = cur;
				cur = cur.next;
			}
		}
		return head;
	}
	
	public static void main(String[] args) {
		ReverseLinkedList obj = new ReverseLinkedList();
		Node head = obj.new  Node(2);
		head.next = obj.new Node(1);
		head.next.next = obj.new Node(2);
		head.next.next.next = obj.new Node(1);
		head.next.next.next.next = obj.new Node(0);
		head.next.next.next.next.next = obj.new Node(0);
		
		Seggregate012 obj1 = new Seggregate012();
		head = obj1.seggregation(head,2);
		head = obj1.seggregation(head,1);
		head = obj1.seggregation(head,0);
		while(head != null) {
			System.out.print(head.data + " ");
			head = head.next;
		}
		System.out.println();
		

	}

}
