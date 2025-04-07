/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
let maxVol = 0 

let i = 0

let j = height.length - 1 


while (j>i) {
    let currentVol =  ( j-i )  * Math.min(height[i], height[j] )

    maxVol = Math.max(maxVol,currentVol)
    
    if (height[i] > height[j]){
        j = j-1
    }
    else{
        i = i+1 
    }



}
return maxVol;
};