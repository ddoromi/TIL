package ch01_Class;

public class Code01 {

	public static void main(String[] args) {
		
		Person1 first;
		first = new Person1();	// object, Person1 주소가 저장됨.
		 
		first.name = "ddorom";
		first.number = "01029806198";
		
		System.out.println(first.name + ": " + first.number);
		
		Person1 [] members = new Person1 [10];
		members[0] = first;
		members[1] = new Person1();
		members[1].name = "taeyoung";
		members[1].number = "01012345678";
		
		System.out.println(members[1].name + ": " + members[1].number);
	}

}
