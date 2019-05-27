import java.util.Scanner;

public class Code02 {
	
	public static void main(String[] args) {
		
		int number = 123;
		Scanner keyboard = new Scanner(System.in);
		System.out.print("please enter an integer: ");
		int input = keyboard.nextInt();
		if(input == number) {
			System.out.println("Numbers match!");
		} else {
			System.out .println("Numbers do not match!");
		}
		
		keyboard.close();
	}
}
