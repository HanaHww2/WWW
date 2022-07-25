package programmers.week5;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=java
 */
public class Ponkemon {

	public int solution(int[] nums) {

		int[] distinct = Arrays.stream(nums)
				.distinct()
				.sorted()
				.toArray();

		return Math.min(nums.length / 2, distinct.length);
	}

	public int withHashSet(int[] nums) {

		Set<Integer> ponkemons = new HashSet<>();

		for (int num : nums) {
			ponkemons.add(num);
		}

		return Math.min(nums.length / 2, ponkemons.size());
	}
}
