class student:
    def __init__(self):
        self.student_id = None
        self.marks = None
        self.age = None
        
    def setter(self):
        self.student_id = input("Enter student_id: ")
        self.marks = int(input("Enter marks: "))
        self.age = int(input("Enter age: "))
        
    def validate_marks(self):
        if self.marks>=0 and self.marks<=100:
            return True
        else:
            print("Invalid data: Marks should in range from 0 to 100!")
        
    def validate_age(self):
        if self.age>20:
            return True
        else:
            print("Invalid data: Age should be 20 or above!")

    def check_qualification(self):
        if(self.validate_marks() and self.validate_age()):
            if self.marks>=65:
                return True
            else:
                return False
        else:
            return False

    def getter(self):
        print("\n\tStudent Details")
        print("Student Id:",self.student_id)
        print("Marks:",self.marks)
        print("Age:",self.age)
        if(obj.check_qualification()):
            print("Qualified!")
        else:
            print("Disqualified!")
        

obj = student()      
obj.setter()
obj.getter()


