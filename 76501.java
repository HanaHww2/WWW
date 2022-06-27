class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int num = absolutes.length;
        
        int answer = 0;
        for(i=0;i<num;i++){
            if(signs[i]=1){
                answer =+ absolutes[i];
            }else{
                answer =- absolutes[i];
            }
        }
        return answer;
    }
}