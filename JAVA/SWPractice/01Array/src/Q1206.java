import java.io.FileInputStream;
import java.util.Scanner;

public class Q1206 {

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("Q1206.txt"));
		Scanner sc = new Scanner(System.in);

		for (int test_case = 1; test_case <= 10; test_case++) {
			int n = sc.nextInt();
			int [] numbers = new int [n];
			int result = 0;
			
			for (int i = 0; i < n; i++)
				numbers[i] = sc.nextInt();

			for (int i = 2; i < n - 2; i++) {
				if (numbers[i] > numbers[i - 1] && numbers[i] > numbers[i - 2]) {
					if (numbers[i] > numbers[i + 1] && numbers[i] > numbers[i + 2]) {
						int max = 0;
						for (int j = -2; j < 3; j++) {
							if (j == 0) 
								continue;
							if (numbers[i + j] > max) 
								max = numbers[i + j];
						}
						result += numbers[i] - max;
					}
				}
			}
			System.out.println("#" + test_case + " " + result);
		}
	}
}
