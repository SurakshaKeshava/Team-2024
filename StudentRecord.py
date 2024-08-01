import csv
import sys
import logging

# Setting up logging to write debug and higher level messages to 'Log.log' with timestamp and log level.
logging.basicConfig(level=logging.DEBUG, filename='Log.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')


class StudentScore:
    """
    A class to manage student records in a CSV file.

    This class provides following operations:
    - Store student data
    - Retrieve student data by roll number
    - Exit the application

    Attributes:
        file_name (str): The name of the CSV file used to store student records.
        csv_file (TextIO): A file object representing the CSV file.

    """
    def __init__(self, file_name):
        """
        Initializes the StudentScore class with the specified CSV file.

        Opens the CSV file in read mode and sets up the file object for later use.
        Logs a message indicating success or an error if the file doesn't exist.

        :param file_name: The name of the CSV file.

        """
        self.file_name = file_name
        try:
            self.csv_file = open(file_name, mode='r', newline='')
            logging.info(f"{file_name} opened Successfully")

        except Exception as e:
            logging.error(f"Error while opening the file {e}")
            print(f"Error while opening the file {e}")
            sys.exit()

    def retrieve_student_score(self, roll_no):
        """
        Retrieves and prints the student record for the given roll number.

        :param roll_no: The roll number of the student whose record is to be retrieved.
        :return: None

        """
        self.csv_file.seek(0)
        reader = csv.DictReader(self.csv_file)
        for student in reader:
            if student['Rollno'] == roll_no:
                print(student)
                return
        print(f"No records found for rollno: {roll_no}")
        logging.error(f"No records found for rollno: {roll_no}")

    def store_student_score(self):
        """
        Displays a menu for managing student data.

        Menu provides options to:
        1. Entering the student data
        2. Save the entered student details
        3. Back to Mainmenu

        :return:None

       """
        logging.debug("Entering StoreStudentScore method.")
        while True:
            print("\n*********** MENU ***********")
            print("1. Enter the Student data")
            print("2. Save the details")
            print("3. Back to mainmenu")

            choice = input("Enter your choice (1/2/3): \n >>>")
            if choice == '1':
                self.enter_data()
            elif choice == '2':
                self.save()
            elif choice == '3':
                return
            else:
                logging.warning("Invalid choice entered in menu.")
                print("Invalid choice. Please enter 1, 2, or 3.")

    def enter_data(self):
        """
        Prompts the user to enter student data and stores it in the instance variable.

        :return:None

        """
        logging.debug("Entering enter_data method.")
        self.student_data={
            'Rollno': input("Enter the Student Rollno: "),
            'name': input("Enter Student Name: ").capitalize(),
            'english': input("Enter English Score: "),
            'maths': input("Enter Maths Score: "),
            'science': input("Enter Science Score: ")
        }
        logging.debug(f"Student data entered: {self.student_data}")

    def save(self):
        """
        Saves the student data to the CSV file if it is valid and rollno does not already exist.

        Checks if the student's roll number already exists in the CSV file. If not, it appends the student data to
        the file. If any data fields are missing or empty, it logs an error and notifies the user.

        :return:None

        """
        logging.debug("Entering save method.")
        self.csv_file.seek(0)
        reader = csv.DictReader(self.csv_file)
        try:
            not all(self.student_data.values()) == True
        except:
            print("No data entered. Student data cannot be empty")
            logging.error("No data entered. Student data cannot be empty")
            return

        if any(row['Rollno'] == self.student_data['Rollno'] for row in reader):
            print(f"Rollno already exists: {self.student_data['Rollno']}")
            logging.error(f"Rollno already exists: {self.student_data['Rollno']}")
            return

        if all(self.student_data.values()):
            with open(file_name, mode='a', newline='') as file:
                fieldnames = ['Rollno', 'name', 'english', 'maths', 'science']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(self.student_data)
            print("Stored successfully")
        else:
            logging.error("Failed to store. Some fields are missing or empty")
            print("Failed to store. The following fields are missing or empty: ", end=' ')
            for key, value in self.student_data.items():
                if not value:
                    print(key, end=', ')

    def exit(self):
        """
        Exits the application and logs an exit message.

        Displays a “Thank You” message to the user and terminates the program execution.
        The termination is achieved by calling sys.exit(), which ends the process.

        :return:None

        """
        logging.info("Exiting the application.")
        print("*********** Thank You ***********")
        sys.exit()

    def main_menu(self):
        """
        Displays the main menu and processes user choices to perform various operations.

        The menu provides options to:
        1. Retrieve student data
        2. Store student data
        3. Exit the application

        The method continues to run in a loop until the user chooses to exit.

        :return: None

        """
        while True:
            print("\n*********** MENU ***********")
            print("1. Retrieve Student Data")
            print("2. Store Student Data")
            print("3. Exit")
            choice = input("Enter your choice (1/2/3): \n >>>")

            if choice == '1':
                roll_no = input("Enter Rollno: ")
                self.retrieve_student_score(roll_no)
            elif choice == '2':
                self.store_student_score()
            elif choice == '3':
                self.exit()
            else:
                logging.warning("Invalid Choice entered in MainMenu")
                print("Invalid choice. Please enter 1, 2 or 3.")


file_name = "Student_data.csv"
student = StudentScore(file_name)
student.main_menu()

