package ch02_schedulerprogram;

public class DeadlinedTask extends Event{
	public MyDate deadline;
	
	public DeadlinedTask(String title, MyDate d) {
		super(title);
		deadline = d;
	}
	
	public String toString() {
		return title + ", " +  " ~ " + deadline.toString();
	}

}
