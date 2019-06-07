package ch02_Method;

public class MyRectangle2 {
	
	public MyPoint2 lu;
	public int width;
	public int height;

	public MyRectangle2(int x, int y, int w, int h) {
		lu = new MyPoint2(x, y);
		width = w;
		height = h;
	}
	
	public int calArea() {
		return width * height;
	}
	
	public String toString() {
		return "LU = (" + lu.x + ", " +lu.y + "), width = " + width + ", height" + height;
	}
}
