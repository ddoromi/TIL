
public class Code01 {
	
	static int num;
	
	public static void main(String[] args) {
		
		int anotherNum = 5;
		num = 2;
		
		System.out.println(num + anotherNum);
		System.out.println("Num: " + num);		// �ڵ����� ���ڿ� ��ȯ
		System.out.println("AnotherNum: " + anotherNum);
		System.out.println("Sum: " + num + anotherNum);		// ���ʿ��� ���ʴ�� ���� �� => (Sum: 2) + 5
	}  

}
