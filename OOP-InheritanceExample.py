# super class, parent class, father class
class Doctor:
    # initializer 
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    # class method
    def register(self):
        pass

    # class method
    def de_regesiter(self):
        pass

# child class inherits from super class
class HospitalDoctor(Doctor):

    # initializer
    # super.__init__()
    def __init__(self, name, phone, email, staff_no, pager_no):
        super().__init__(name, phone, email)
        self.staff_no = staff_no
        self.pager_no = pager_no

class IntershipDoctor(Doctor):
    pass 

# define an object doctor 
doctor1 = Doctor("David", "0900000000", "davidli@mail.mcu.edu.tw")
print(doctor1.name, doctor1.phone, doctor1.email)

# define an object of hosptial doctor
hospital_doctor1 = HospitalDoctor("Peter", "098877855", "peter@mail.mcu.edu.tw","123456", "1111122222")
print(hospital_doctor1.staff_no, hospital_doctor1.pager_no)



