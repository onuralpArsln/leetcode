class Solution:
    def trap(self, height) -> int:
        total = 0
        left =0
        right = len(height)-1

        leftMax = 0
        rightMax=0

        while left < right:
            if height[left] < height[right]:
                print(f"sağ değer büyük sol oynar,  sağ : {height[right]} sol : {height[left]} ")
                if height[left] > leftMax:
                    print("yeni sol maksı buldum solumda yükse duvar yok su akar eklemem")
                    leftMax =height[left]
                else:
                    total += leftMax - height[left]
                    print(f" cevremde duvar var su tutarım yeni total: {total}")
                
                left +=1
                print("sol pointer oynadı")

            else:
                print(f"sol değer büyük sağ oynar,  sağ : {height[right]} sol : {height[left]} ")
                if height[right] > rightMax:
                    print("yeni sağ maksı buldum sağımda yüksek duvar yok su akar eklemem")
                    rightMax = height[right]
                else:
                    total += rightMax - height[right]
                    print(f" cevremde duvar var su tutarım yeni total: {total}")
                
                right -=1
                print("sağ pointer oynadı")

                
        return total


solver = Solution()


myarray =[0,1,3,1,10,0,10,2,3,1,0,3]

print(myarray)
print(solver.trap(myarray))