

class Patient:
    def __init__(self, p_id, name, age, gender, disease, contact):
        self.p_id = p_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease
        self.contact = contact
        self.doctor_id = None

class Doctor:
    def __init__(self, d_id, name, specialization, contact):
        self.d_id = d_id
        self.name = name
        self.specialization = specialization
        self.contact = contact
        self.patient_id = []


class Hospital:
    def __init__(self):
        self.patients = {}
        self.doctors = {}

    def valid_patient(self, p_id):
        return p_id.isdigit() and 1000 <= int(p_id) <= 4999 and p_id not in self.patients

    def valid_doctor(self, d_id):
        return d_id.isdigit() and 5000 <= int(d_id) <= 9999 and d_id not in self.doctors


    def add_patient(self):
        while True:
            p_id = input("enter patient id (1000-4999)!:")
            if self.valid_patient(p_id):
                break
            print("invalid or duplicate patient id!")

        name = input("enter name:")
        age = input("enter age:")
        gender = input("enter gender:")
        disease = input("enter disease:")
        contact = input("enter contact:")

        self.patients[p_id] = Patient(p_id, name, age, gender, disease, contact)


    def add_doctor(self):
        while True:
            d_id = input("enter doctor id (5000-9999)!:")
            if self.valid_doctor(d_id):
                break
            print("invalid or duplicate doctor id!")

        name = input("enter name:")
        specialization = input("enter specialization:")
        contact = input("enter contact:")

        self.doctors[d_id] = Doctor(d_id, name, specialization, contact)


    def assign_patient(self):
        p_id = input("enter patient id:")
        d_id = input("enter doctor id:")

        if p_id in self.patients and d_id in self.doctors:
            self.doctors[d_id].patient_id.append(p_id)
            self.patients[p_id].doctor_id = d_id
        else:
            print("invalid patient id or doctor id!")


    def view_patient(self):
        p_id = input("enter patient id:")

        if p_id in self.patients:
            p = self.patients[p_id]

            print("-" * 50)
            print("patient details")
            print("-" * 50)

            print(f"id          : {p.p_id}")
            print(f"name        : {p.name}")
            print(f"age         : {p.age}")
            print(f"gender      : {p.gender}")
            print(f"disease     : {p.disease}")
            print(f"contact     : {p.contact}")
            print(f"doctor's id : {p.doctor_id}")
        else:
            print("patient not found!")


    def view_doctor(self):
        d_id = input("enter doctor id!:")
        if d_id in self.doctors:
            d = self.doctors[d_id]

            print("-" * 50)
            print("doctor details!")
            print("-" * 50)
            print(f"id             : {d.d_id}")
            print(f"name           : {d.name}")
            print(f"specialization : {d.specialization}")
            print(f"contact        : {d.contact}")
            print(f"patients's ids : {d.patient_id}")
        else:
            print("doctor not found!")


    def discharge_patient(self):
        p_id = input("enter patient id:")

        if p_id in self.patients:
            d_id = self.patients[p_id].doctor_id
            self.doctors[d_id].patient_id.remove(p_id)
            del self.patients[p_id]
        else:
            print("patient not found!")


    def show_all(self):
        print("patients")
        print("-" * 80)
        print(f"{'p_id':<10}{'name':<15}{'age':<10}{'gender':<10}{'disease':<15}{'doctor_id':<10}")
        print("-" * 80)

        for p in self.patients.values():
            print(f"{p.p_id:<10}{p.name:<15}{p.age:<10}{p.gender:<10}{p.disease:<15}{p.doctor_id}")

        print("doctors")
        print("-" * 80)
        print(f"{'d_id':<10}{'name':<15}{'specialization':<20}{'contact':<15}{'patients_ids':<20}")
        print("-" * 80)

        for d in self.doctors.values():
            print(f"{d.d_id:<10} {d.name:<15} {d.specialization:<20} {d.contact:<15} {d.patient_id}")

def main():
    hospital = Hospital()

    while True:
        print("-" * 50)
        print("1. add patient!")
        print("2. add doctor")
        print("3. assignpatient to doctor!")
        print("4. view patient!")
        print("5. view doctor!")
        print("6. discharge patient!")
        print("7. show all data!")
        print("8. exit!")
        print("-" * 50)

        choice = input("enter your choice!:")

        if choice == "1":
            hospital.add_patient()
        elif choice == "2":
            hospital.add_doctor()
        elif choice == "3":
            hospital.assign_patient()
        elif choice == "4":
            hospital.view_patient()
        elif choice == "5":
            hospital.view_doctor()
        elif choice == "6":
            hospital.discharge_patient()
        elif choice == "7":
            hospital.show_all()
        elif choice == "8":
            print("thank you!")
            break
        else:
            print("invalid choice!")


main()
