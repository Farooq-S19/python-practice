left, right =0,1

prices =[10,1,5,6,7,1]
n =len(prices)
while right<=n-1 and left<=n-1:
    if prices[left]<prices[right]:
        