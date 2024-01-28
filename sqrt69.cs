public class Solution {
    public int MySqrt(int x) {
        
        // assume it is the smallest number with given amount of digits
       // even length 1000 > 4 > even > start from  len / 2 2 
        // odd length 100 >  3 >  odd > start from len / 2  ++ 
        // 10000 5  5/2  2 2++ start from 100
        // 100000 6 
 
        int length= (x.ToString().Length);
        Console.WriteLine("length is " +length);
        
        int rootLength;

        int root = 0;

        if (length % 2 == 0 ){ rootLength = length/2;  }
        else{rootLength = length/2; rootLength++;}

        if(rootLength>1){root=10;
        for(int i=2; i<rootLength; i++){ root = root*10;}}

        Console.WriteLine("rootlength "+ rootLength );

        //  big step forwaard first 
        Console.WriteLine("x is " +x);
        Console.WriteLine("root is " + root);
        int goBig = x/(root+1);
        Console.WriteLine(goBig);
        int fastRoot= root*(goBig.ToString().Length)/2;
        Console.WriteLine("fastRoot "+fastRoot);

        //  do binaet search between fast root and root*10 - 1 

        while( fastRoot*fastRoot < x){ fastRoot++; 
        //Console.WriteLine(fastRoot);
        }


        if(fastRoot*fastRoot > x){return fastRoot-1;}
        else{return fastRoot;}


    }
}
