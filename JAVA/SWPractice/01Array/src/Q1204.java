import java.util.Scanner;
import java.io.FileInputStream;

public class Q1204 {

	public static void main(String[] args) throws Exception {
		
		System.setIn(new FileInputStream("Q1204.txt"));
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++) {
			int t = sc.nextInt();
			int [] scores = new int [1000];
			int [] counts = new int [101];
			int max = 0;
			int result = 0;
		
			for (int i = 0; i < 1000; i++) {
				scores[i] = sc.nextInt();
				counts[scores[i]]++;
			}
			
			for (int i = 100; i >= 0; i--) {
				if (counts[i] > max) {
					max = counts[i];
					result = i;
					
				}
			}
		System.out.println("#" + test_case + " " + result);
		}
	}
}
