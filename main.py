
class Information : # in heritance act as parent class
    def __init__(callback, Name,Academic_Position, Identity_Number , Major, Year):
        callback.Name = Name
        callback.Academic_Position = Academic_Position
        callback.Identity_Number = Identity_Number 
        callback.Major = Major
        callback.Year = Year

class Student(Information) :
    def __init__(callback, Name, Academic_Position,  Identity_Number, Major, year):
        super().__init__(Name, Academic_Position, Identity_Number, Major, year)
    def Instrument(Complement):
        print("--------------Student--------------")
        print("Student Name = " + Complement.Name)
        print("Position in this academic = " + Complement.Academic_Position)
        print("Major = " + Complement.Major)
        print("Identity number = " + Complement.Identity_Number)
        print("Jurusan = " + Complement.Major)

#inheritance 
class Teacher(Information):
    def __init__(callback, Name, Academic_Position, Identify_Number, Major, year):
        super().__init__(Name, Academic_Position, Identify_Number , Major, year)
    def Instrument(Complement):
        print("-------Teacher------")
        print("Teacher Name = " + Complement.Name)
        print("Position in this academic = " + Complement.Academic_Position)
        print("Identity Number = " + Complement.Identity_Number)
        print("Major = " + Complement.Major)
        print("Teaching Year= " + Complement.Year)


Name_Input =  input("Input your Name = ")
Position_Input = input("Input your position in this academic = ")
Identitynumber_Input = input("Input your academic identity number = ")
Major_Input = input("Input your major = ")
Year_Input = input("Input your year = ")


if Position_Input == "teacher" or Position_Input == "Teacher":
    result = Teacher(Name_Input,Position_Input,Identitynumber_Input,Major_Input,Year_Input)
    result.Instrument()
elif Position_Input == "student" or Position_Input == "Student":
    result = Student(Name_Input,Position_Input,Identitynumber_Input,Major_Input,Year_Input)
    result.Instrument()
else :
    print("ERROR // re-input and check your types ")
    
