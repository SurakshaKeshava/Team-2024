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
        2. Exit the application

        The method continues to run in a loop until the user chooses to exit.

        :return: None

        """
        while True:
            print("\n*********** MENU ***********")
            print("1. Retrieve Student Data")
            print("2. Exit")
            choice = input("Enter your choice (1/2): \n >>>")

            if choice == '1':
                roll_no = input("Enter Rollno: ")
                self.retrieve_student_score(roll_no)
            elif choice == '2':
                self.exit()
            else:
                logging.warning("Invalid Choice entered in MainMenu")
                print("Invalid choice. Please enter 1 or 2.")


file_name = "Student_data.csv"
student = StudentScore(file_name)
student.main_menu()

