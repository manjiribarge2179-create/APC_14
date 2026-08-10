prices=(100,250,75,500,150)
total=sum(prices)
average=total/len(prices)
highest=prices[0]
lowest=prices[0]
for price in prices:
    if price>highest:
        highest=price
    if price<lowest:
        lowest=price
print("Total bill:",total)
print("Average price:",average)
print("Highest price:",highest)
print("Lowest price:",lowest)