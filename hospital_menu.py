class User:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact


class Patient(User):
    def __init__(self, patient_id, name, age, disease, contact):
        super().__init__(name, contact)
        self.patient_id = patient_id
        self.age = age
        self.disease = disease
        self.doctors = []

class Doctor(User):
    def __init__(self, doc_id, name, specialization, contact):
        super().__init__(name, contact)
        self.doc_id = doc_id
        self.specialization = specialization

patients = {}
doctors = {}
patient_id = 1000
doc_id = 2000

while True:
    print("Menu")
    print("1 Add Patient")
    print("2 Add Doctor")
    print("3 Assign Doctor")
    print("4 View Patient")
    print("5 View Doctor")
    print("6 Discharge Patient")
    print("7 Show All Records")
    print("8 Exit")

    choice = input("Enter choice: ")
# 1 Add Patient
    if choice == "1":
        name = input("Name: ")
        age = input("Age: ")
        disease = input("Disease: ")
        contact = input("Contact: ")

        p = Patient(patient_id, name, age, disease, contact)
        patients[patient_id] = p
        print("Patient Added with ID:", patient_id)
        patient_id += 1

# 2 Add Doctor
    elif choice == "2":
        name = input("Name: ")
        specialization = input("Specialization: ")
        contact = input("Contact: ")

        d = Doctor(doc_id, name, specialization, contact)
        doctors[doc_id] = doc_id
        print("Doctor Added with ID:", doc_id)
        doc_id += 1

# 3 Assign Doctor
    elif choice == "3":
        patient_id = int(input("Patient ID: "))
        doc_id = int(input("Doctor ID: "))

        if patient_id in patients and doc_id in doctors:
            patients[patient_id].doctors.append(doc_id)
            print("Doctor Assigned")
        else:
            print("Invalid ID")

# 4 View Patient
    elif choice == "4":
        patient_id = int(input("Patient ID: "))

        if patient_id in patients:
            p = patients[patient_id]
            print("Name:", p.name)
            print("Age:", p.age)
            print("Disease:", p.disease)
            print("Contact:", p.contact)
            print("Doctors:", p.doctors)
        else:
            print("Patient Not Found")

# 5 View Doctor
    elif choice == "5":
        d_id = int(input("Doctor ID: "))

        if doc_id in doctors:
            doctors[doc_id] = d  
            print("Name:", d.name)
            print("Specialization:", d.specialization)
            print("Contact:", d.contact)
        else:
            print("Doctor Not Found")

# 6 Discharge Patient
    elif choice == "6":
        patient_id = int(input("Patient ID: "))

        if patient_id in patients:
            del patients[patient_id]
            print("Patient Discharged")
        else:
            print("Patient Not Found")

# 7 Show All
    elif choice == "7":
        print("\nPatients:")
        for p in patients.values():
            print(p.patient_id, p.name, p.disease)

        print("\nDoctors:")
        for d in doctors.values():
            print(d.doc_id, d.name, d.specialization)

# 8 Exit
    elif choice == "8":
        print("Bye Bye")
        break

    else:
        print("Invalid Choice")
