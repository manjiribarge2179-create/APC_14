patients=((101,"Gauri",20,"A+"),(102,"Amit",25,"B+"),(103,"Sneha",22,"O+"),(104,"Rahul",30,"A+"))
print("All patient records:")
for patient in patients:
    print(patient)
patient_id=int(input("Enter patient ID to search: "))
found=False
for patient in patients:
    if patient[0]==patient_id:
        print("Patient found:",patient)
        found=True
if not found:
    print("Patient not found")
print("Total patients:",len(patients))
blood=input("Enter blood group: ")
print("Patients with",blood,"blood group:")
for patient in patients:
    if patient[3]==blood:
        print(patient)