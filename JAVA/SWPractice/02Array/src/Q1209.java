import java.util.Scanner;
import java.io.FileInputStream;

public class Q1209 {

	public static void main(String[] args) throws Exception {
		
		System.setIn(new FileInputStream("Q1209.txt"));
		Scanner sc = new Scanner(System.in);

		for(int test_case = 1; test_case <= 10; test_case++) {
			int t = sc.nextInt();
			int [][] data = new int [100][100];
			int max = 0;
			
			for (int x = 0; x < 100; x++) {
				for (int y = 0; y < 100; y++) {
					data[x][y] = sc.nextInt();
				}
			}
			
			int sum3 = 0;
			
			for (int x = 0; x < 100; x++) {
				int sum1 = 0;
				int sum2 = 0;
				sum3 += data[x][x];
				
				for (int y = 0; y < 100; y++) {
					sum1 += data[x][y];
					sum2 += data[y][x];
				}
				
				if (sum1 > max) max = sum1;
				if (sum2 > max) max = sum2;
			}
			if (sum3 > max) max = sum3;
		System.out.println("#" + t + " " + max);
		}
	}
}