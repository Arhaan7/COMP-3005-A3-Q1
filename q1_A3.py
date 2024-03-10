# Arhaan Wazid
# Student ID: 101256222

import psycopg2
from psycopg2 import sql

# Connect to an existing database
def connect():
    #connect to the database
    conn = psycopg2.connect(
        # loading all the information to connect to the database
        # TAs please change the user and password to your own to test the code
        user="postgres",
        password="carleton",
        host="localhost",
        port = "5432",
        database="Question1_A3"
    )
    return conn


# function that gets all the students from the database
def getAllStudents():
    #connect to the database
    conn = connect()
    #create a cursor object
    cur = conn.cursor()
    #execute a SELECT statement
    cur.execute("SELECT * FROM students")
    #retrieve the results
    rows = cur.fetchall()
    #print the results
    for row in rows:
        print(row)
    #close the cursor and the connection
    cur.close()
    conn.close()

# function that adds a student to the database
def addStudent(first_name, last_name, email, enrollment_date):
    #connect to the database
    conn = connect()
    #create a cursor object
    cur = conn.cursor()
    #execute an INSERT statement
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    #commit the transaction
    conn.commit()
    #close the cursor and the connection
    cur.close()
    conn.close()

# function that updates a student's email in the database
def updateStudentEmail(student_id, email):
    #connect to the database
    conn = connect()
    #create a cursor object
    cur = conn.cursor()
    #execute an UPDATE statement
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (email, student_id))
    #commit the transaction
    conn.commit()
    #close the cursor and the connection
    cur.close()
    conn.close()

# function that deletes a student from the database
def deleteStudent(student_id):
    #connect to the database
    conn = connect()
    #create a cursor object
    cur = conn.cursor()
    #execute a DELETE statement
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    #commit the transaction
    conn.commit()
    #close the cursor and the connection
    print("Deleted student with id: ", student_id)
    #close the cursor and the connection
    cur.close()
    conn.close()

def main():

    #creating menu for user thats repeat until user exits
    print("Welcome to the Student Management System by Arhaan Wazid!")

    while True:
        #menu options
        print("1. Get all students")
        print("2. Add a student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("0. Exit")

        #prompting user for input of choice
        choice = input("Enter your choice: ")

        #if statements to call the functions based on user input
        if choice == "1":
            #call the function to get all students
            getAllStudents()
        elif choice == "2":
            #prompt the user for the student's information
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            email = input("Enter the student's email: ")
            enrollment_date = input("Enter the student's enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == "3":
            #prompt the user for the student's id and new email
            student_id = input("Enter the student's id: ")
            email = input("Enter the student's new email: ")
            updateStudentEmail(student_id, email)
        elif choice == "4":
            #prompt the user for the student's id
            student_id = input("Enter the student's id: ")
            deleteStudent(student_id)
        elif choice == "0":
            #exit the program
            break
        else:
            #if the user enters an invalid choice
            print("Invalid choice")

# call the main function
if __name__ == '__main__':
    main()