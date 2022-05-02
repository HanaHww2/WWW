import java.io.IOException;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;

class DDOROREE_Solution {
	static HashSet<Integer> combinationNumbers = new HashSet<Integer>();
    static boolean[] check = new boolean[10000000];
    static String[] rawsNumbers;
	static boolean[] visitedDigit;
    
    public int solution(String numbers) {
		// 소수 미리 구해놓기
		check[0] = check[1] = true;
		
        // 에라토스테네스의 체
		for( int i=2;i<check.length;i++ ) {
			if( !check[i] ) {
				for( int j=i*2;j<check.length;j+=i ) {
					check[j] = true;
				}
			}
		}

		rawsNumbers = numbers.split("");
		visitedDigit = new boolean[rawsNumbers.length]; // 2만큼
				
		// 숫자 조합 만들기 - 순열 - 돌아가면서 앞자리 세우기 식으로..
		dfs(0,"");

        return combinationNumbers.size();
	}
	
	public static void dfs(int digit, String number) {
        if ( digit > rawsNumbers.length ){
        	return;
        }
        
        if( number!="" && !check[Integer.parseInt(number)] ) {
			combinationNumbers.add( Integer.parseInt(number) );
		}
        
        for( int i=0;i<rawsNumbers.length;i++ ){ //0, 2
        	if ( !visitedDigit[i] ) {  // 한번 사용된 요소는 다시 사용하면 안되므로 필터링
        		visitedDigit[i] = true;
				dfs( digit+1,number+rawsNumbers[i] );
				visitedDigit[i] = false;
        	}
        }
	}
    
    
    
    
}