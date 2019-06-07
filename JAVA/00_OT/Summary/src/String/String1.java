package String;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class String1 {

	static String [] words = new String [100000];
	static int [] count = new int [100000];
	static int n = 0;

	static void makeIndex(String fileName) {
		try {
			Scanner inFile = new Scanner(new File(fileName));
			while (inFile.hasNext()) {
				String str = inFile.next();
				addWord(str);
			}
			inFile.close();

		} catch (FileNotFoundException e) {
			System.out.println("No File");
			return;
		}
	}

	static void addWord(String str) {
		int index = findWord(str);		// return -1 if not find
		if (index != -1) {		
			count[index]++; 
		} 
		else {
			words[n] = str;
			count[n] = 1;
			n++;
		}
	}

	static int findWord(String str) {
		for (int i = 0; i < n; i++) 
			if (words[i].equals(str))
				return i;
		return -1;
	}

	static void saveAs(String fileName) {
		try {
			PrintWriter out = new PrintWriter(new FileWriter(fileName));
			for (int i = 0; i < n; i++) {
				out.println(words[i] + " " + count[i]);
			}
			out.close();
		} 
		catch (IOException e) {
			System.out.println("Save falied.");
			return;
		}
	}

	public static void main(String[] args) {

		Scanner keyboard =  new Scanner(System.in);

		while (true) {
			System.out.print("$ ");
			String command = keyboard.next();

			if (command.equals("read")) {
				String fileName = keyboard.next();
				makeIndex(fileName);
			}
			else if (command.equals("find")) {
				String str = keyboard.next();
				int index = findWord(str);
				if (index != -1) {
					System.out.println("The word " + words[index] + " appears " + count[index] + " times.");
				}
				else {
					System.out.println(str + " does not appear.");
				}
			}
			else if (command.equals("saveas")) {
				String fileName = keyboard.next();
				saveAs(fileName);
			}
			else if(command.equals("exit")) {
				break;
			}
		}
		keyboard.close();
	}
}
