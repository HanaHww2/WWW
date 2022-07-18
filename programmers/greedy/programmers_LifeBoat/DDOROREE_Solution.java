/**
 * 
 */
package Level_2.greedy;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class DDOROREE_Solution {
    public int solution(int[] people, int limit) {        
        int result = 0;

		Arrays.sort(people);
		
		Deque<Integer> peopleDeque = new ArrayDeque<Integer>(50001);
		
		for( int weight : people ) {
			peopleDeque.add(weight);
		}
		
		 while( !peopleDeque.isEmpty()  ) {
            result++;
            int currentPerson = peopleDeque.pollLast();
            if( !peopleDeque.isEmpty() && currentPerson+peopleDeque.peekFirst()<=limit ) {
                peopleDeque.pollFirst();
            }
        }
        
        return result;
    }
}
