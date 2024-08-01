import csv
import logging

# Setting up logging to write debug and higher level messages to 'Log.log' with timestamp and log level.
logging.basicConfig(level=logging.DEBUG, filename='Log.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')


class StudentScore:
    """
    A class to manage student records in a CSV file.

    This class provides following operation:
    - Retrieve student data by roll number

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


file_name = "Student_data.csv"
student = StudentScore(file_name)
roll_no = input("Enter the Rollno: ")
student.retrieve_student_score(roll_no)






















