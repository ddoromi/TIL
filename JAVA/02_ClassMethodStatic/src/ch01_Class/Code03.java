package ch01_Class;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Code03 {
	
	static Person1 [] members = new Person1 [100];
	static int n = 0;
	
	static void bubbleSort() {
		for (int i = n - 1; i > 0; i--) {
			for (int j = 0; j < 1; j++) {
				if(members[j].name.compareTo(members[j + 1].name) > 0) {
					Person1 tmp = members[j];
					members[j] = members[j + 1];
					members[j + 1] = tmp;
				}
			}
		}
	}
	
	public static void main(String[] args) {
		
		try {
			Scanner in = new Scanner(new File("input.txt"));

			while(in.hasNext()) {
				String name = in.next();
				String number = in.next();
				
				members[n] = new Person1();
				members[n].name = name;
				members[n].number = number;
				n++;
			}
			in.close();
		} 
		catch (FileNotFoundException e) {
			System.out.println("No File");
		}
		
		bubbleSort();
		for (int i = 0; i < n; i++)
			System.out.println(members[i].name + ", " + members[i].number);
	}
}
