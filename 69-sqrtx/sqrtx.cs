public class Solution {
    public int MySqrt(int x) {

        int digit = x.ToString().Length;
        
        /*
        4 digit 
        min 1000 root 31 
        max 9999 root 100

        5 digit 
        min 10000 root 100
        max 99999 316 
        */

        int minRootDigit;
        
        if(digit % 2 == 0){ 
             minRootDigit = digit/2;
            int maxRootDigit = (digit / 2 ) ;

        }
        else {
             minRootDigit = (digit+1)/2;
            int maxRootDigit = (digit+1)/2;

        }

        long min=1;
        long max=10;

        for(int i = 1 ; i < minRootDigit; i++){
            min*=10;
            max*=10;
        }
        Console.WriteLine("calculated min" + min);
        Console.WriteLine("calculated max" + max);

        //if(digit%2==0){min*=3;}else{max*=4;}
        
       long mid =  (max + min) / 2;
        long  midsq = mid*mid;

        while (min <= max)
        {
             mid = (min + max) / 2;
             midsq = mid*mid;

           

            // Check if target is present at mid
            if (midsq == x)
                return (int)mid;

            // If target greater, ignore left half
            else if ( x >= midsq ){
                Console.WriteLine("min arttı  "+ (x-(midsq)) + " midsq val: " + midsq);
                min = mid +1 ;
                Console.WriteLine(min);
               }
            // If target is smaller, ignore right half
            else{
            Console.WriteLine("max azaldı");
                max = mid - 1;}
        }
        

        if (midsq>x) return (int)mid-1;
        return (int)mid;


        
    }
}