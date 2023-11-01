isStock = False #şuan elinde stok var mı 
profit = 0  #kar
currentStock = 0 # mevcut stok değeri

prices = [7,1,5,3,6,4]

days = len(prices)


for i in range(days):
    # son güne geldiysen 
    if  i == days-1:
        if isStock and currentStock < prices[i]:
            profit  += prices[i]-currentStock
    # son günde değilsen
    else:
        # eğer elinde varsa ve fiyat yarın düşecekse sat 
        if isStock and prices[i+1] < prices[i]:
            profit  += prices[i]-currentStock
            isStock = False
            currentStock = 0
        # eğer elinde yoksa ve fiyat artacaksa al
        elif isStock== False  and prices[i+1] >  prices[i]:
            currentStock = prices[i]
            isStock= True
    print("day is" + str(i+1))
    print("isStock")
    print(isStock)
    
    print(profit)
    print()

print(profit)