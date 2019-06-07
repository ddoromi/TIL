package ch01_Class;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class IndexMaker {

	static Item [] items = new Item [1000000];
	static int n = 0;

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
					System.out.println("The word " + items[index].word + " appears " + items[index].count + " times.");
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
			items[index].count++; 
		} 
		else {
			int i = n - 1;
			while (i >= 0 && items[i].word.compareTo(str) > 0) {
				items[i + 1] = items[i];
				i--;
			}
			items[i + 1] = new Item();
			items[i + 1].word = str;
			items[i + 1].count = 1;
			n++;
		}
	}

	static int findWord(String str) {
		for (int i = 0; i < n; i++) 
			if (items[i].word.equals(str))
				return i;
		return -1;
	}

	static void saveAs(String fileName) {
		try {
			PrintWriter out = new PrintWriter(new FileWriter(fileName));
			for (int i = 0; i < n; i++) {
				out.println(items[i].word + " " + items[i].count);
			}
			out.close();
		} 
		catch (IOException e) {
			System.out.println("Save falied.");
			return;
		}
	}
}