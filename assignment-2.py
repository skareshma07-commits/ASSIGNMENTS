students = {}

while True:
    print("\n******** STUDENT MANAGEMENT SYSTEM ********")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. Find Average Marks")
    print("8. Count Students")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))
        students[roll] = {"Name": name, "Marks": marks}
        print("Student Added Successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Details:")
            for roll, details in students.items():
                print("Roll No:", roll)
                print("Name:", details["Name"])
                print("Marks:", details["Marks"])
                print("----------------------")

    elif choice == 3:
        roll = input("Enter Roll Number to Search: ")
        if roll in students:
            print("Student Found!")
            print("Name:", students[roll]["Name"])
            print("Marks:", students[roll]["Marks"])
        else:
            print("Student Not Found!")

    elif choice == 4:
        roll = input("Enter Roll Number: ")
        if roll in students:
            new_marks = float(input("Enter New Marks: "))
            students[roll]["Marks"] = new_marks
            print("Marks Updated Successfully!")
        else:
            print("Student Not Found!")

    elif choice == 5:
        roll = input("Enter Roll Number to Delete: ")
        if roll in students:
            del students[roll]
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    elif choice == 6:
        if len(students) == 0:
            print("No student records available.")
        else:
            topper_roll = max(students, key=lambda x: students[x]["Marks"])
            print("\nTopper Details:")
            print("Roll No:", topper_roll)
            print("Name:", students[topper_roll]["Name"])
            print("Marks:", students[topper_roll]["Marks"])

    elif choice == 7:
        if len(students) == 0:
            print("No student records available.")
        else:
            total = 0
            for details in students.values():
                total += details["Marks"]
            average = total / len(students)
            print("Average Marks =", average)

    elif choice == 8:
        print("Total Students =", len(students))

    elif choice == 9:
        print("Thank You! Exiting Student Management System...")
        break

    else:
        print("Invalid Choice! Please try again.")
