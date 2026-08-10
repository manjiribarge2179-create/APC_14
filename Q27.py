tuple1=(10,20,30,40)
tuple2=(30,40,50,60)
merged=tuple1+tuple2
unique=[]
for num in merged:
    if num not in unique:
        unique.append(num)
merged=tuple(unique)
print("Merged tuple without duplicates:",merged)