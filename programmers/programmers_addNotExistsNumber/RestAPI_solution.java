/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/86051
 */
public class AddNotExistsNumber {

	public int solution(int[] numbers) {
		int sum = 0;

		for (int num : numbers) {
			sum += num;
		}

		return 45 - sum;
	}

	public static void main(String[] args) {
		AddNotExistsNumber solution = new AddNotExistsNumber();
		System.out.println(solution.solution(new int[] {1, 2, 3, 4, 6, 7, 8, 0}));
	}
}
