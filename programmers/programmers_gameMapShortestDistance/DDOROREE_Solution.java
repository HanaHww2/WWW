import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

class POSITION {
	int x;
	int y;

	public POSITION(int x, int y) {
		super();
		this.x = x;
		this.y = y;
	}
}

class Solution {
	public int solution(int[][] maps) {
		int[] dx = {-1, 1, 0, 0}, dy = {0, 0, -1, 1}; // 좌표평면

		Queue<POSITION> queue = new LinkedList<POSITION>();

		int N = maps.length;
		int M = maps[0].length;

		boolean[][] check = new boolean[N][M];		// 방문 여부 배열
		int[][] distance = new int[N][M];			// 거리에 따른 증가 배열

		/* 시작 위치에 대한 초기값 설정*/
		queue.add(new POSITION(0, 0));
		check[0][0] = true;
		distance[0][0] = 1;
		
		/* 게임 진행 */
		while (!queue.isEmpty()) {
			POSITION currentPosition = queue.poll(); // 큐에서 빼면서 다음 타겟으로 전진한 셈.

			for (int i = 0; i < 4; i++) {
				int sideX = dx[i] + currentPosition.x;
				int sideY = dy[i] + currentPosition.y;
				if (sideX >= 0 && sideX < N && sideY >= 0 && sideY < M
					&& !check[sideX][sideY]
					&& maps[sideX][sideY] == 1) {
					check[sideX][sideY] = true;
					queue.add(new POSITION(sideX, sideY)); // 다음에 갈 타겟 좌표를 큐에 넣는 것.
					distance[sideX][sideY] = distance[currentPosition.x][currentPosition.y] + 1; // 현재 좌표값의 누적거리값에서 +1
				}
			}

		}

        return distance[N-1][M-1]==0?-1:distance[N-1][M-1];
	}
}