import java.util.ArrayDeque;
import java.util.Queue;

import Stack_Queue.LEVEL_2.Pair;

class Pair{
    int index;
    int value;

    public Pair(int index, int value) {
        this.index = index;
        this.value = value;
    }
}

class Solution {
    public int solution(int[] priorities, int location) {
        int			result	= 0; 
		Pair		target	= null;
		Queue<Pair> queue	= new ArrayDeque<Pair>();
		
		for( int i=0;i<priorities.length;i++ ){
			queue.offer( new Pair(i,priorities[i]) );
			if( i==location ) {
				target = new Pair(i,priorities[i]);
			}
		}
		
		while( !queue.isEmpty() ) {
			boolean isExistMaxValue = false;
			Pair	currentPriority = queue.poll();
			
			// 한번 더 돌면서 하나라도 현재 값보다 큰 우선순위가 있는지 찾고 없으면 끝까지 돈다.
			for( Pair comparePriority : queue ){
				if( currentPriority.value < comparePriority.value ){
					isExistMaxValue = true;
					break;
				}
			}
			
			if( !isExistMaxValue ) {
				result++;
				
				if( currentPriority.index==location ) {
					break;
				}
				
				// 가장 큰 우선순위는 poll 된 후 다시 추가하지 않도록 하기 위함
				if( currentPriority.value!=target.value ) {
					continue;
				}
			}
			
			queue.offer( currentPriority );
		}
		
        return result;
    }
}