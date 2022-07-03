import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;


class Solution {
	public List<String> solution(String[] orders, int[] course) {
		static boolean[] visitedDigit;
		static Map<Integer, Map<String,Integer>>	courses		= new HashMap<Integer, Map<String,Integer>>();
		static int[]								courseMax	= new int[11]; // course의 경우에 따라 구한 조합들 중 가장 많이 주문된 횟수를 저장.
		
		List<String> result = new ArrayList<String>();

		for( int c : course ){
			courses.put( c, new HashMap<String,Integer>() );
			for( int i=0;i<orders.length;i++ ) {
				String[] splitOrder = orders[i].split("");
				visitedDigit = new boolean[splitOrder.length]; // order별로 방문 자릿수 체크 배열을 새로 생성
				dfs( splitOrder, 0, 0, c, "" );
			}
		}
		
		for( int count : courses.keySet() ){
			Map<String, Integer> temp = courses.get(count);
			for( String key : temp.keySet() ){
				int maxCount	= courseMax[key.length()];
				int	currentCount= temp.get(key);
				// 최소 2명 이상의 손님에게서 주문된 구성만 코스요리 후보 && 현재 코스의 최대 요리개수와 같크
				if( currentCount>1 && (maxCount<currentCount||maxCount==currentCount) ){
					result.add(key);
				}
			}
		}
		
		result.sort(null);
		
		return result;
	}
		
	private static void dfs(String[] splitOrder, int startIndex, int digit, int currentCourseCount, String temp) {
		if( digit == currentCourseCount ){ // 증가 자리수==코스 음식 개수
			char[] tempArray =  temp.toCharArray();
			Arrays.sort(tempArray);
			temp = new String(tempArray);
			
			Map<String, Integer> combinationSet	= courses.get(currentCourseCount);
			
			if( combinationSet!=null && combinationSet.containsKey(temp) ){
				int currentCount = combinationSet.get(temp);
				combinationSet.put( temp, currentCount+1 );
				if( courseMax[digit]<currentCount+1 ) {
					courseMax[digit] = currentCount+1;
				}
				return;
			}
			
			combinationSet.put( temp, 1 );
		}
		
		for( int i=startIndex;i<=splitOrder.length-1;i++ ){
			if ( !visitedDigit[i] ) {		// 한번 사용된 요소는 다시 사용하면 안되므로 필터링
	    		visitedDigit[i] = true;		// 재귀 들어가기 전에 T를 해줘서 다음 문자가 같은 게 오지 않도록 하기 위함
				dfs( splitOrder, i+1, digit+1, currentCourseCount, temp+splitOrder[i] );
				visitedDigit[i] = false;	// 빠져나온 후에는 F를 해줘서 다음 턴에서 앞에 오는 문자들이 다시 올 수 있도록 풀어줌.
	    	}
		}
		
	}
		
}