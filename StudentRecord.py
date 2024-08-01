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
    - Store student data
    - Calculate and update average scores for students
    - Display all student records sorted by a specified header
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
            logging.warning(f"Rollno already exists: {self.student_data['Rollno']}")
            return

        if all(self.student_data.values()):
            with open(file_name, mode='a', newline='') as file:
                fieldnames = ['Rollno', 'name', 'english', 'maths', 'science']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(self.student_data)
            print("Stored successfully")
        else:
            logging.warning("Failed to store. Some fields are missing or empty")
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

    def average(self):
        """
        Calculates and adds the average score for each student to the CSV file.

        Reads student scores from the CSV file, computes the average score for
        English, Maths, and Science for each student, and writes the updated data
        back to the CSV file with an additional 'Average' column.

        If the 'Average' column is not already present in the CSV, it is added.

        :return:None

        """
        logging.debug("Entering average method.")
        self.csv_file.seek(0)
        reader = csv.DictReader(self.csv_file)
        rows = list(reader)
        fieldnames = reader.fieldnames

        if 'Average' not in fieldnames:
            fieldnames.append('Average')
        try:
            for row in rows:
                english_score = float(row['english'])
                maths_score = float(row['maths'])
                science_score = float(row['science'])

                total = english_score + maths_score + science_score
                count = 3
                avg = total / count
                row['Average'] = round(avg, 2)
        except ValueError as e:
            print(f"ValueError: {e}")
            logging.error(f"ValueError: {e}")
            return

        with open(file_name, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print("Average added successfully")
        logging.info("Average added successfully")

    def display_all(self, header, ascending=True):
        """
        Displays all student records sorted by the specified header.

        Reads student records from the CSV file, sorts them based on the provided
        header in either ascending or descending order, and prints the sorted
        records.

        :param header: The column name by which to sort the records.
        :param ascending: Indicates the sort order (True for ascending, False for descending). Defaults to True.
        :return: None

        """
        logging.debug("Entering display_all method")
        self.csv_file.seek(0)
        reader = csv.DictReader(self.csv_file)
        rows = list(reader)
        fieldnames = reader.fieldnames

        if header not in fieldnames:
            logging.error(f"Error: Provided header '{header}' does not match any CSV column.")
            print(f"Error: Provided header '{header}' does not match any CSV column.")
            return

        rows.sort(key=lambda row: int(row[header]) if row[header].isdigit() else row[header], reverse=not ascending)

        print("".join(fieldnames))
        for row in rows:
            print(','.join(str(row[field]) for field in fieldnames))


    def main_menu(self):
        """
        Displays the main menu and processes user choices to perform various operations.

        The menu provides options to:
        1. Retrieve student data
        2. Store student data
        3. Calculates the Average
        4. Display all student records sorted by a specified header
        5. Exit the application

        The method continues to run in a loop until the user chooses to exit.

        :return: None

        """
        while True:
            print("\n*********** MENU ***********")
            print("1. Retrieve Student Data")
            print("2. Store Student Data")
            print("3. Calculate Average")
            print("4. Display Sort Records")
            print("5. Exit")
            choice = input("Enter your choice (1/2/3/4/5): \n >>>")

            if choice == '1':
                roll_no = input("Enter Rollno: ")
                self.retrieve_student_score(roll_no)
            elif choice == '2':
                self.store_student_score()
            elif choice == '3':
                self.average()
            elif choice == '4':
                header = input("Enter header: ")
                ascending = input("Sort order (True/False)?: ").strip().lower() in ['true', 1, '']
                self.display_all(header, ascending)
            elif choice == '5':
                self.exit()
            else:
                logging.warning("Invalid Choice entered in MainMenu")
                print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")


if __name__ == "__main__":
    file_name = "Student_data.csv"
    student = StudentScore(file_name)
    try:
        student.main_menu()
    finally:
        student.csv_file.close()
        logging.info(f"Closing {file_name}")

