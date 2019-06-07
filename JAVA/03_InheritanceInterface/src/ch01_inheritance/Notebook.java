package ch01_inheritance;

public class Notebook extends Computer{
	private double screenSize;
	private double weight;

	public Notebook(String man, String proc, int ram, int disk, double procSpeed, double screen, double weight) {
		super(man, proc, ram, disk, procSpeed);
		screenSize = screen;
		this.weight = weight;
	}
	
	public String toString() {
		String result = super.toString() + 
						"\nScreen Size: " + screenSize + "inches" +
						"\nWeight: " + weight + "kg";
		return result;
	}
	
	public static void main(String [] args) {
		Computer test = new Notebook("Dell", "i5", 4, 1000, 3.2, 5.6, 1.2);
		System.out.println(test.toString());
		
		// static binding => compiler가 결정권을 갖는 경우
		// dynamic binding => runtime 할 때 결정하는 경우 <= JAVA
	}
}

