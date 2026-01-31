'''
Hospital Management System

This program implements a basic Hospital Management System using
Python.
Features:
1. Add Patient

2. Add Doctor

3. Assign Doctor to Patient

4. View Doctor Details

5. Discharge Patient
   
6. Display Hospital Records'''  

class Patient_details:

    def __init__(self, pat_id, name, age , gender, disease , contact_no):
        self.pat_id = pat_id
        self.name = name
        self.age = age
        self.contact_no = contact_no
        self.disease = disease
        self.gender = gender
        self.doctor_id = None

        
class Doctor_details:

    def __init__(self, doc_id, name, specialzation ,  contact_no ):
        self.doc_id = doc_id
        self.specialization = specialzation
        self.name = name
        self.contact_no = contact_no


class Hospital:
    def __init__(self):
        self.patients = {}
        self.doctors = {}


    def valid_4_digit_id(self, value):
        return value.isdigit() and len(value) == 4
    
    def add_patient(self):
        pat_id = input("Enter Patient ID (4 digits): ").strip()
        if not self.valid_4_digit_id(pat_id):
            print("Patient ID must be 4 digits")
            return
        
        if pat_id in self.patients:
            print(" Patient ID already exists")
            return
        
        name = input("Name: ").strip()

        if not name:
            print("Name cannot be empty")
            return
        
        age = input("Age: ")

        if not age.isdigit() or int(age) <= 0:
            print("Invalid age")
            return
        age = int(age)


        gender = input("Enter gender (Male/ Female / Other) ").lower()

        if gender not in ["male", "female", "other"]:
            print(" Invalid gender")
            return


        disease = input("Disease: ").strip()
        contact_no = input("Contact (10 digits): ")


        if not contact_no.isdigit() or len(contact_no) != 10:
            print("Invalid contact number")
            return
        
        self.patients[pat_id] = Patient_details(pat_id, name, age, gender, disease, contact_no)
        print("Patient added successfully")

    def add_doctor(self):
        doc_id = input("Enter Doctor ID (4 digits): ").strip()

        if not self.valid_4_digit_id(doc_id):
            print("Doctor ID must be exactly 4 digits")
            return
        if doc_id in self.doctors:
            print("Doctor ID already exists")
            return
        
        name = input("Name: ").strip()
        specialization = input("Specialization: ").strip()
        contact_no = input("Contact (10 digits): ")

        if not contact_no.isdigit() or len(contact_no) != 10:
            print("Invalid contact number")
            return
        
        self.doctors[doc_id] = Doctor_details(doc_id, name, specialization, contact_no)
        print(" Doctor added successfully")

    def assign_doctor(self):
        pat_id = input("Enter Patient ID: ")
        doc_id = input("Enter Doctor ID: ")

        if pat_id not in self.patients:
            print("Patient not found")
            return

        if doc_id not in self.doctors:
            print("Doctor not found")
            return

        # One patient cannot have multiple doctors
        if self.patients[pat_id].doctor_id is not None:
            print(" Patient already has a doctor assigned")
            return

        self.patients[pat_id].doctor_id = doc_id
        print("Doctor assigned successfully")


    def view_patient(self):
        pat_id = input("Enter Patient ID: ")
        if pat_id not in self.patients:
            print("Patient not found")
            return

        p = self.patients[pat_id]
        print("\n--- Patient Details ---")
        print(f"ID       : {p.pat_id}")
        print(f"Name     : {p.name}")
        print(f"Age      : {p.age}")
        print(f"Gender   : {p.gender}")
        print(f"Disease  : {p.disease}")
        print(f"Contact  : {p.contact_no}")
        print(f"DoctorID : {p.doctor_id}")


    def view_doctor(self):
        doc_id = input("Enter Doctor ID: ")
        if doc_id not in self.doctors:
            print(" Doctor not found")
            return

        d = self.doctors[doc_id]
        print("\n--- Doctor Details ---")
        print(f"ID             : {d.doc_id}")
        print(f"Name           : {d.name}")
        print(f"Specialization : {d.specialization}")
        print(f"Contact        : {d.contact_no}")

    def discharge_patient(self):
        pat_id = input("Enter Patient ID to discharge: ")
        if pat_id not in self.patients:
            print(" Patient not found")
            return

        del self.patients[pat_id]
        print("Patient discharged successfully")



    def show_all(self):
        if not self.patients and not self.doctors:
            print("⚠ No data available")
            return

        print("\nPATIENT TABLE")
        print("-" * 90)
        print("PAT_ID  Name      Age Gender Disease       Contact     DoctorID")
        print("-" * 90)
        for p in self.patients.values():
            print(f"{p.pat_id:<8} {p.name:<12} {p.age:<6} {p.gender:<10} "
                  f"{p.disease:<15} {p.contact_no:<15} {p.doctor_id:<10}")

        print("\nDOCTOR TABLE")
        print("-" * 70)
        print(f"{'DOC_ID':<8}{'Name':<12}{'Specialization':<20}{'Contact':<15}")
        print("-" * 70)
        for d in self.doctors.values():
             print(f"{d.doc_id:<8}{d.name:<12}{d.specialization:<20}{d.contact_no:<15}")
             
    def menu(self):
        print("""
=========== Hospital Management ===========
1. Add Patient
2. Add Doctor
3. Assign Doctor to Patient
4. View Patient Detail
5. View Doctor Detail
6. Discharge Patient
7. Show All Data
8. Exit
==========================================
""")
        
def main():
    hospital = Hospital()

    while True:
        hospital.menu()
        choice = input("Enter your choice: ")

        if not choice.isdigit() or int(choice) not in range(1, 9):
            print("Please select a valid option (1-8)")
            continue

        if choice == "1":
            hospital.add_patient()
        elif choice == "2":
            hospital.add_doctor()
        elif choice == "3":
            hospital.assign_doctor()
        elif choice == "4":
            hospital.view_patient()
        elif choice == "5":
            hospital.view_doctor()
        elif choice == "6":
            hospital.discharge_patient()
        elif choice == "7":
            hospital.show_all()
        elif choice == "8":
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()