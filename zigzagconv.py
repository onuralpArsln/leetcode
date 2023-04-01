
word = 'PAYPALISHIRING'
numRows = 3 
resArr = []


for i in range(2*numRows-2):
    resArr.append(word[i::2*numRows-2])
    print(resArr[i])



    

for i in range(numRows):
    if i==0 :
        res = res+resArr[0]
    elif i < numRows-1:
        for i in range(numRows-2):
            counter = (2*numRows-3)-i
            print(counter)
            for j in range(len(resArr[counter])):
                res = res+ resArr[i+1][j]
                res = res + resArr[counter][j]
                print(len(resArr[counter]))
            if(len(resArr[counter]) < len(resArr[i+1])):
                res = res + resArr[i+1][-1]
    elif i == numRows-1:   
        res = res+ resArr[numRows-1]
print(res)
    
