package ch01_Class;

public class Code01_2 {

	public static void main(String[] args) {
		Person1 first = new Person1();
		first.name = "John";
		first.number = "0511233456";
		
		Person1 second = first;
		second.name = "kwon";
		System.out.println(first.name + ", " + first.number);
		
		Person1 [] members = new Person1 [100];		// �迭�� �� ĭ�� Ÿ���� Person1������ ���� �����̹Ƿ� ��ü�� ���� ��������� ��.
		members[0] = first;
		members[1] = new Person1();		// Person1�� ���ο� ��ü�� ������.
		members[1].name = "David";
		members[1].number = "044444534";
		
		System.out.println(members[1].name + ", " + members[1].number);
	}

}
