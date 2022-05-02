import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class DDOROREE_Solution {
	public Integer[] solution(int[] progresses, int[] speeds) {
		List<Integer> days = new ArrayList<Integer>();
		Queue<Integer> queue = new LinkedList<Integer>();

		for (int i = 0; i < speeds.length; i++) {
			int currentDeployDate = (int)Math.ceil((100 - progresses[i]) / (double)speeds[i]); // 완료일 계산하는 거
			if (!queue.isEmpty() && queue.peek() < currentDeployDate) {
				days.add(queue.size());
				queue.clear();
			}
			queue.offer(currentDeployDate);
		}

		days.add(queue.size());

		Integer[] result = days.toArray(new Integer[] {days.size()}); // 리스트 -> 배열
		return result;
	}
}