class Hospital:
    def __init__(self):
        self.patients = {}
        self.doctors = {}

    
    def add_patient(self):
        pid = input("Patient ID:")

        if pid in self.patients:
            print("Patients already axists")
            return
        
        Name  = input("Name:")
        Age = input("Age:")
        Gender = input("Gender:")
        Disease = input("Disease:")
        Contact = input("Contact:")

        self.patients[pid] = {
            "Name" : Name,
            "Age" : Age,
            "Gender" : Gender,
            "Disease" : Disease,
            "Contact": Contact,
            "Doctor":None
        }

        print("Patients Added")

    def add_doctor(self):
        did = input("Doctor ID:")

        if did not in self.doctors:
            Name = input("Doctor Name:")
            Spec = input("Specialization:")
            Contact = input("Contact")

            self.doctors[did] = {
                "Name" : Name,
                "Specialization" : Spec,
                "Contact" : Contact,
                "Patients" : []
            }
            print("Doctor Added")
        else:
            print("Doctor already exists")

    def assign_doctor(self):
        pid = input("Patient ID:")
        did = input("Doctor ID:")

        if pid in self.patients and did in self.doctors:
            self.patients[pid]["Doctor"] = did
            self.doctors[did]["Patients"].append(pid) 
            print("Doctor Assigned")
        else:
            print("Wrong patient ID and Doctor ID")

    def view_patient(self):
        pid = input("Patient ID:")

        if pid in self.patients:
            print("\nPatient Detail")
            print("----------------")
            for k , v in self.patients[pid].items():
                print(k ,":" ,v)
        else:
            print("Patient not found")

    def doctor_details(self):
        for did in self.doctors:
            d = self.doctors[did]

            print("\n{:^40}".format(d["Name"]))
            print("-"*40)

            for pid in d["Patients"]:
                p = self.patients[pid]
                print("Patient ID:",pid)
                print("Name      :",p["Name"])
                print("Age       :",p["Age"])
                print("Gender    :",p["Gender"])
                print("Disease   :",p["Disease"])
                print("Contact   :",p["Contact"])
                print("-"*40)

    def discharge_patient(self):
        pid = input("Patient ID:")

        if pid in self.patients:
            did  = self.patients[pid]["Doctor"]

            if did:
                self.doctors[did]["patient"].remove[pid]
            
            del self.patients[pid]
            print("Patient Discharged")
        
        else:
            print("Patient not found")

h = Hospital()

while True:
    print("\n======== MENU ========")
    print("1 Add Patient")
    print("2 Add Doctor")
    print("3 Assign Doctor")
    print("4 View Patient")
    print("5 Doctor Detail")
    print("6 Discharg Patient")
    print("7 Exit")

    ch = input("Enter choice:")

    if ch == "1":
        h.add_patient()
    elif ch == "2":
        h.add_doctor()
    elif ch == "3":
        h.assign_doctor()
    elif ch == "4":
        h.view_patient()
    elif ch == "5":
        h.doctor_details()
    elif ch == "6":
        h.discharge_patient()
    elif ch == "7":
        print("Exit programs")
        break
    else:
        print("Wrong choice")
