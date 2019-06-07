
public class List {

	public static void main(String[] args) {

		int [] grades;
		grades = new int[5];	// int [] grades = new int[5];

		grades[0] = 100;
		grades[1] = 6;
		grades[2] = 4;
		grades[3] = 76;
		grades[4] = 14;

		for (int i = 0; i < grades.length; i++) {
			System.out.println("Grade" + (i+1) + ": " + grades[i]);
		}

		int i = 0;

		while(i < grades.length) {
			System.out.println(grades[i]);
			i++;
		}
	}
}

