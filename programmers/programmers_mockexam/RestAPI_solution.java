import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MockExam {

	public int[] solution(int[] answers) {

		int[] person1 = {1, 2, 3, 4, 5};
		int[] person2 = {2, 1, 2, 3, 2, 4, 2, 5};
		int[] person3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

		int max;
		int[] scores = new int[3];

		for (int i = 0; i < answers.length; i++) {
			if (answers[i] == person1[i % person1.length]) {
				scores[0]++;
			}

			if (answers[i] == person2[i % person2.length]) {
				scores[1]++;
			}

			if (answers[i] == person3[i % person3.length]) {
				scores[2]++;
			}
		}

		max = Math.max(scores[0], (Math.max(scores[1], scores[2])));

		List<Integer> list = new ArrayList<>();

		for (int i = 0; i < scores.length; i++) {
			if (max == scores[i]) {
				list.add(i + 1);
			}
		}

		return list.stream()
				.mapToInt(i -> i)
				.toArray();
	}

	public static void main(String[] args) {
		MockExam solution = new MockExam();
		System.out.println(Arrays.toString(solution.solution(new int[] {1, 2, 3, 4, 5})));
	}
}
