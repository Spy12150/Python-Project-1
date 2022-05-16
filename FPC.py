# FPC = Final Project Classes, shortened so I don't have to type 20 letters every time
# Ideas worked on:
# Enroll student/teacher, details, login system, ID random gen, assign assignments from teacher that students can see
# Questions: Class variables in relation to child classes - what to move over

# Requirements: pip install pwinput
import pwinput
import datetime
import time
# Bold Text
B1 = "\033[1m"
B2 = "\033[0;0m"

class School:
    def __init__(self, name, enrollment, classes, location, students=[], faculty=[]):
        self.name = name
        self.enrollment = enrollment
        self.classes = classes
        self.location = location
        self.students = students
        self.faculty = faculty
    
    def main_menu(self):
        print("qwer")

    def print_enrollment(self):
        print(f"There are {self.enrollment} students at {self.name}.")
    
    def print_location(self):
        print(f"The school is located at {self.location}.")

    def enroll_student(self):
        print("Please register your student below: \n")
        current_student = Person()
        self.students.append(current_student.first_name+" "+current_student.last_name)
        School.main_menu()
        

class Person:
    def __init__(self, age = None, gender = "None Found", \
                address = "None Found", phone_number = "None Found"):
        self.first_name = (input("Please enter this person's first name: ")).title()
        self.last_name = (input("Please enter this person's last name: ")).title()
        self.age = age
        self.address = address
        self.gender = gender
        self.phone_number = phone_number

    def confirmation(self):
        print(f"{self.first_name} {self.last_name} has been successfully registered.\n")

    def check_details(self):
        print(f"\nYour current Details are listed as: \
        \n\nFirst name: {self.first_name} \
        \nLast name: {self.last_name} \
        \nAge: {self.age} \
        \nAddress: {self.address} \
        \nGender: {self.gender}\
        \nPhone Number: {self.phone_number} \n\
        \n1 - Edit Information\
        \n2 - Return to Menu")
        v3 = input("Input: ")
        if v3 == 1:
            Person.edit_details()
        if v3 == 2:
            Student.student_menu()

    def edit_details(self):
        print("Which information would you like to edit?\n\
        \n1 - First name: {self.first_name} \
        \n2 - Last name: {self.last_name} \
        \n3 - Age: {self.age} \
        \n4 - Address: {self.address} \
        \n5 - Gender: {self.gender} \
        \n6 - Phone Number: {self.phone_number} \
        \n7 - EXIT\n")
        
        while True:
            edit_index = input("Please enter the number corresponding to the option you wish to edit.")
            if edit_index == 1:
                self.first_name = input("Please enter your first name: ").title()
                Person.edit_details()
            if edit_index == 2:
                self.last_name = input("Please enter your last name: ").title()
                Person.edit_details()
            if edit_index == 3:
                self.age = input("Please enter your age: ")
                Person.edit_details()
            if edit_index == 4:
                self.address = Person.input_address()
                Person.edit_details()
            if edit_index == 5:
                self.gender = input("Please enter your gender: ")
                Person.edit_details()
            if edit_index == 6:
                self.phone_Number = input("Please enter your Phone number: ")
                Person.edit_details()
            if edit_index == 7:
                break
        print("\nreturning...\n")
        time.sleep(1)
        Student.student_menu()
        
    # returning value from function
    def input_address(self):
        street = input("Please input the street number and  street name: ")
        city = input("Please enter the city: ")
        state = input("Please enter the state: ")
        zip = input("Please enter the zip code: ")
        return f"{street} {city} {state} {zip}"

    def edit_password(self):
        print("Placeholder for edit_password")
        self.student_menu()

class Student(Person):
    def __init__(self, grade,  graduation, GPA, ID, age = None, gender = "None Found", \
                address = "None Found", phone_number = "None Found"):
        self.grade = grade
        self.graduation = graduation
        self.GPA = GPA
        self.ID = ID
        Person.__init__(self, age = None, gender = "None Found", address = "None Found", phone_number = "None Found")
        # demonstrating selecting parts of string
        self.email = self.first_name[:1].lower() + self.last_name.lower() + str(self.graduation) + "@gmail.com"
        print(f"\n{self.first_name} {self.last_name} has been successfully registered as a student.\n")
        print(f"Welcome to myschoolapp, {self.first_name}!")

    def assignment_menu(self):
        print(f"{B1}Assignments{B2}")
    
    def student_menu(self):
        time.sleep(0.5)
        print(f'\n\n{B1}MAIN MENU{B2} \n\nIt is currently {str(datetime.datetime.now())[:16]}\
            \n\nPlease choose an option:\
            \n1. View Assignments\
            \n2. View Profile\
            \n3. Change Password\
            \n4. Log Out\n')

        student_value = input("Option: ")
        if student_value == "1":
            self.assignment_menu()
        if student_value == "2":
            self.check_details()
        if student_value == "3":
            self.edit_password()
        if student_value == "4":
            School.main_menu()
            
            
class faculty(Person):
    def __init__(self, subject, years_employed, age = None, gender = "None Found", \
                address = "None Found", phone_number = "None Found"):
        self.subject = subject
        self.years_employed = years_employed
        self.email = self.first_name[:1].lower() + self.last_name.lower() + "@gmail.com"
        Person.__init__(self, age = None, gender = "None Found", address = "None Found", phone_number = "None Found")
        print(f"{self.first_name} {self.last_name} has been successfully registered as a faculty.\n")

class Assignment:
    def __init__(self, title, type, course, due_date, assign_date, status):
        self.title = title
        self.type = type
        self.course = course
        self.due_date = due_date
        self.assign_date = assign_date
        self.status = status
    
if __name__ == '__main__':
    x = Student(2,23,4,5)
    x.student_menu()