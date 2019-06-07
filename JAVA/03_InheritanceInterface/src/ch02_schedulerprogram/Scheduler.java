package ch02_schedulerprogram;

import java.util.Scanner;

public class Scheduler {
	
	
	private int capacity = 10;
	Event [] events = new Event [capacity];
	int n = 0;
	private Scanner kb;
	
	public void processCommand() {
		kb = new Scanner(System.in);
		
		while(true) {
			System.out.print("$ ");
			String command = kb.next();
			
			if (command.equals("addevent")) {
				String type = kb.next();
				if(type.equalsIgnoreCase("oneday")) {
					handleAddOneDayEvent();
				}
				else if(type.equalsIgnoreCase("duration")) {
					handleAddDurationEvent();
				} 
				else if(type.equalsIgnoreCase("deadline")) {
					handleAddDeadlineEvent();
				}
			}
			else if (command.equals("list")) {
				handleList();
			}
			else if (command.equals("show")) {
				
			}
			else if (command.equals("exit")) {
				break;
			}
		}
		kb.close();
	}
	

	private void handleList() {
		for (int i = 0; i < n; i++) {
			System.out.println("   " + events[i].toString());
		}
	}


	private MyDate parseDateString(String dateString) {
		String [] tokens = dateString.split("/");
		
		int year = Integer.parseInt(tokens[0]);
		int month = Integer.parseInt(tokens[1]);
		int day = Integer.parseInt(tokens[2]);
		
		return new MyDate(year, month, day);
	}
	
	private void addEvent(Event ev) {
		if (n >= capacity)
			reallocate();
		events[n++] = ev;
	}

	private void reallocate() {
		Event [] tmp = new Event [capacity * 2];
		for (int i = 0; i < n; i++)
			tmp[i] = events[i];
		capacity *= 2;
	}
	
	private void handleAddOneDayEvent() {
		System.out.print(" when: ");
		String dateString = kb.next();
		System.out.print(" title: ");
		String title = kb.next();
		
		MyDate date = parseDateString(dateString);
		OneDayEvent ev = new OneDayEvent(title, date);
		addEvent(ev);
	}


	private void handleAddDeadlineEvent() {
		System.out.print(" deadline: ");
		String dateString = kb.next();
		System.out.print(" title: ");
		String title = kb.next();
		
		MyDate date = parseDateString(dateString);
		DeadlinedTask ev = new DeadlinedTask(title, date);
		addEvent(ev);
	}

	private void handleAddDurationEvent() {
		System.out.print(" begin: ");
		String beginDate = kb.next();
		System.out.print(" end: ");
		String endDate = kb.next();
		System.out.print(" title: ");
		String title = kb.next();
		
		MyDate begin = parseDateString(beginDate);
		MyDate end = parseDateString(endDate);
		
		DurationEvent ev = new DurationEvent(title, begin, end);
		addEvent(ev);
	}

	public static void main(String [] args) {
		Scheduler app = new Scheduler();
		app.processCommand();
	}
}
