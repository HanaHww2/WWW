import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        int max = citations.length; // 예외가 없다면 적어도 논문 개수만큼 다 인용되도록 하기 위함
        
		Arrays.sort(citations);
        
        // 내림차순
		for( int i=citations.length-1;i>=0;i-- ){
			int currentCitation = citations[i];
			if( currentCitation<=citations.length-1-i ){ // 4-4 -> 4-3 -> 4-3 -> 4-2 -> 4-1 -> 4-0
				max = citations.length-1-i; // 해당 인덱스 리턴
				break;
			}
		}
        
        return max;
    }
}