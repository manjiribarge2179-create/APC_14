temperatures=(28,31,29,35,32,30,27)
maximum=temperatures[0]
minimum=temperatures[0]
for temp in temperatures:
    if temp>maximum:
        maximum=temp
    if temp<minimum:
        minimum=temp
average=sum(temperatures)/len(temperatures)
print("Maximum temperature:",maximum)
print("Minimum temperature:",minimum)
print("Average temperature:",average)