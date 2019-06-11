package ch03_ObjectWrapperclass;

public class Test {
	public int a = 10;
	public double x = 12.45;
	
	public String toString() {
		return a + " " + x;
	}
	
	public boolean equals(Test t) {
		return (a == t.a && x == t.x);
	}
	
	public static void main(String [] args) {
		Test test = new Test();
		Test test2 = new Test();
		
		test2.a = 10;
		test2.x = 12.45;
		
		System.out.println(test.toString());
		
		if(test2.equals(test))
			System.out.println("yes");
		else
			System.out.println("no");
	}
}
