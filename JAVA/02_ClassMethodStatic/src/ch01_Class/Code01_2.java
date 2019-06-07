package ch01_Class;

public class Code01_2 {

	public static void main(String[] args) {
		Person1 first = new Person1();
		first.name = "John";
		first.number = "0511233456";
		
		Person1 second = first;
		second.name = "kwon";
		System.out.println(first.name + ", " + first.number);
		
		Person1 [] members = new Person1 [100];		// 배열의 각 칸의 타입은 Person1이지만 찹조 변수이므로 객체는 따로 저장해줘야 함.
		members[0] = first;
		members[1] = new Person1();		// Person1의 새로운 객체를 참조함.
		members[1].name = "David";
		members[1].number = "044444534";
		
		System.out.println(members[1].name + ", " + members[1].number);
	}

}
