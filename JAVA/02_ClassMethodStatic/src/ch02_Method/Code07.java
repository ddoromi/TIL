package ch02_Method;

import java.util.Scanner;

public class Code07 {

	static Polynomial3 [] polys = new Polynomial3 [100];
	static int n = 0;
	
	public static void main(String[] args) {
	
		Scanner kb = new Scanner(System.in);
		while(true) {
			System.out.print("$ ");
			String command = kb.next();
			
			if (command.contentEquals("create")) {
				char name = kb.next().charAt(0);
				polys[n] = new Polynomial3(name);
				n++;
			}
			else if (command.contentEquals("add")) {
				char name = kb.next().charAt(0);
				int index = find(name);
				if (index == -1) {
					System.out.println("No such polynomial exists.");
				}
				else {
					int c = kb.nextInt();
					int e = kb.nextInt();
					polys[index].addTerm(c, e);
				}
			}
			else if (command.equals("calc")) {
				char name = kb.next().charAt(0);
				int index = find(name);
				if (index == -1) {
					System.out.println("No such polynomial exists.");
				}
				else {
					int x = kb.nextInt();
					int result = polys[index].calcPolynomial(x);
					System.out.println(result);
				}
			}
			else if (command.equals("print")) {
				char name = kb.next().charAt(0);
				int index = find(name);
				if (index == -1) {
					System.out.println("No such polynomial exists.");
				}
				else {
					polys[index].printPolynomial();
				}
			}
			else if (command.equals("exit"))
				break;
		}
	}
	
	private static int find(char name) {
		for (int i = 0; i < n; i++)
			if (polys[i].name == name)
				return i;
		return -1;
	}
}
