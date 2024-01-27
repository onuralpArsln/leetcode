public class Solution {
    public int SearchInsert(int[] nums, int target) {
        int currentIndex = 0;
        
        foreach ( int number in nums ) {
            currentIndex ++ ;
            Console.WriteLine(currentIndex);
            if( number >= target  ) {
                currentIndex -- ;
                break;

            }
        }
        return  currentIndex;
    }
}