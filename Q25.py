runs=(45,78,120,34,56,102,89,150,42,67)
total=sum(runs)
highest=runs[0]
lowest=runs[0]
for run in runs:
    if run>highest:
        highest=run
    if run<lowest:
        lowest=run
average=total/len(runs)
print("Total runs:",total)
print("Highest score:",highest)
print("Lowest score:",lowest)
print("Average score:",average)