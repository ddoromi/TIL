import java.io.FileInputStream;
import java.util.Scanner;

public class Q1201 {
	
	static int [][] data;
	static int result = 100;

	public static void main(String[] args) throws Exception {
		
		System.setIn(new FileInputStream("Q1201.txt"));
		Scanner sc = new Scanner(System.in);
		
		for (int test_case = 0; test_case < 1; test_case++) {
			int t = sc.nextInt();
			data = new int [100][100];
			
			for (int x = 0; x < 100; x++) {
				for (int y = 0; y < 100; y++) {
					data[x][y] = sc.nextInt();
				}
			}
			
			for (int x = 0; x < 100; x++) {
				if (data[99][x] == 2) {
					findLadder(99, x);
				}
			}
			System.out.println("#" + t + " " + result);
		}
	}

	private static void findLadder(int x, int y) {
		if (x == 0) {
			result = y;
		}
		
		data[x][y] = 3;
		int [][] delta = {{x - 1, y}, {x, y - 1}, {x, y + 1}};
		
		for (int i = 0; i < 4; i++) {
			if (delta[i][0] == -1 || delta[i][1] == -1 || delta[i][0] == 100 || delta[i][1] == 100)
				continue;
			if (data[delta[i][0]][delta[i][1]] == 1) {
				findLadder(delta[i][0], delta[i][1]);
			}
		}
	}
}
