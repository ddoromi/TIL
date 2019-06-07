
public class Code01 {
	
	static int num;
	
	public static void main(String[] args) {
		
		int anotherNum = 5;
		num = 2;
		
		System.out.println(num + anotherNum);
		System.out.println("Num: " + num);		// 자동으로 문자열 변환
		System.out.println("AnotherNum: " + anotherNum);
		System.out.println("Sum: " + num + anotherNum);		// 왼쪽에서 차례대로 연산 됨 => (Sum: 2) + 5
	}  

}
