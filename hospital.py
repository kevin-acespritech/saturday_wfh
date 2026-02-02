class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class Patient(Person):
    def __init__(self, pid, name, age, gender, disease, contact):
        super().__init__(name, contact)
        self.pid = pid
        self.age = age
        self.gender = gender
        self.disease = disease
        self.doctors = []

class Doctor(Person):
    def __init__(self, did, name, specialization, contact):
        super().__init__(name, contact)
        self.did = did
        self.specialization = specialization

patients = {}
doctors = {}

def generate_id(store):
    i = 1000
    while i in store:
        i += 1
    return i

def add_patient():
    name = input("Name : ")
    age = input("Age : ")
    gender = input("Gender : ")
    disease = input("Disease : ")
    contact = input("Contact : ")

    pid = generate_id(patients)
    patients[pid] = Patient(pid, name, age, gender, disease, contact)

    print("Patient added successfully. ID =", pid)

def add_doctor():
    name = input("Name : ")
    specialization = input("Specialization : ")
    contact = input("Contact : ")

    did = generate_id(doctors)
    doctors[did] = Doctor(did, name, specialization, contact)

    print("Doctor added successfully. ID =", did)

def assign_doctor():
    pid = int(input("Enter patient id : "))
    did = int(input("Enter doctor id : "))

    if pid in patients and did in doctors:
        if did not in patients[pid].doctors:
            patients[pid].doctors.append(did)
            print("Doctor assigned successfully")
        else:
            print("Doctor already assigned")
    else:
        print("Invalid patient or doctor ID")

def view_patient():
    pid = int(input("Enter patient id : "))

    if pid in patients:
        p = patients[pid]
        print("\nPatient ID :", p.pid)
        print("Name :", p.name)
        print("Age :", p.age)
        print("Gender :", p.gender)
        print("Disease :", p.disease)
        print("Contact :", p.contact)

        print("Doctors :")
        if not p.doctors:
            print("None")
        else:
            for d in p.doctors:
                print(d, "-", doctors[d].name)
    else:
        print("Patient not found")

def view_doctor():
    did = int(input("Enter doctor id : "))

    if did in doctors:
        d = doctors[did]
        print("\nDoctor ID :", d.did)
        print("Name :", d.name)
        print("Specialization :", d.specialization)
        print("Contact :", d.contact)
    else:
        print("Doctor not found")

def discharge_patient():
    pid = int(input("Enter patient id : "))

    if pid in patients:
        del patients[pid]
        print("Patient discharged successfully")
    else:
        print("Patient not found")

def table_view():
    print("\n----- PATIENT TABLE -----")
    if not patients:
        print("No patients available")
    else:
        print("{:<6} {:<15} {:<15} {:<20}".format("ID", "Name", "Disease", "Doctors"))
        for p in patients.values():
            names = ""
            for d in p.doctors:
                names += doctors[d].name + ", "
            names = names.rstrip(", ") or "None"

            print("{:<6} {:<15} {:<15} {:<20}".format(p.pid, p.name, p.disease, names))

    print("\n----- DOCTOR TABLE -----")
    if not doctors:
        print("No doctors available")
    else:
        print("{:<6} {:<15} {:<20}".format("ID", "Name", "Specialization"))
        for d in doctors.values():
            print("{:<6} {:<15} {:<20}".format(d.did, d.name, d.specialization))

while True:
    print("\n----- MENU -----")
    print("1. Add patient")
    print("2. Add doctor")
    print("3. Assign doctor to patient")
    print("4. View patient detail")
    print("5. View doctor detail")
    print("6. Discharge patient")
    print("7. Table view")
    print("8. Exit")

    choice = input("Enter choice : ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        add_doctor()
    elif choice == "3":
        assign_doctor()
    elif choice == "4":
        view_patient()
    elif choice == "5":
        view_doctor()
    elif choice == "6":
        discharge_patient()
    elif choice == "7":
        table_view()
    elif choice == "8":
        print("Thank you")
        break
    else:
        print("Invalid choice")


