
import time  # Importing time module to allow time breaks between print statements (Mainly for better user experience)
print("Welcome to Phys 102 grades calculation project.")
time.sleep(2)

# Introducing the capabilities of our program
print("You can calculate your personal letter grade and see the whole class statistics.")
time.sleep(2)

# Determining the mode of the program (Personal Grade Calculation or Whole Class Statistics)
Mode = input("For personal grade calculation enter \"1\":\nFor whole class statistics enter \"2\": ")

# Making sure the user enters a valid response
while Mode != "1" and Mode != "2":
    Mode = input("Error! For personal grade calculation enter \"1\":\nFor whole class statistics enter \"2\": ")


if Mode == "1":
    # The user chose Personal Grade Calculation
    from Functions_Personnal_Grade import*  # Importing the functions file for personal grade calculation

    # Informing the user about which data they will need to provide in order to determine their grade
    print("To calculate your grade, you will need to provide your:")
    time_wait(0.5)
    print("1- First midterm grade.")
    time_wait(1)
    print("2- Second midterm grade.")
    time_wait(1)
    print("3- Five quiz grades.")
    time_wait(1)
    print("4- Fourteen assignment grades.")
    time_wait(1)
    print("5- Final grade.")
    time_wait(2)

    # Prompting the user to enter midterm 1 grade
    MT = float(input("Enter midterm1 grade: "))
    # Making sure the user enters a correct midterm  grade (Between 0 and 100)
    if MT < 0 or MT > 100:
        MT = correct_MT1(MT)

    # Prompting the user to enter midterm 2 grade
    MT2 = float(input("Enter midterm2 grade: "))
    # Making sure the user enters correct midterm 2 grade (Between 0 and 100)
    if MT2 < 0 or MT2 > 100:
        MT2 = correct_MT2(MT2)

    # Prompting the user to enter their 5 quiz grades
    Quiz = input("Enter quizzes grades: ").split()
    # Making sure the user enters EXACTLY 5 quizzes each of which is within range 0 to 10
    if len(Quiz) != 5 or any(int(i) < 0 for i in Quiz) or any(int(i) > 10 for i in Quiz):
        Quiz = correct_Quiz(Quiz)

    # Prompting the user to enter their 14 assignment grades
    Assignment = input("Enter assignments grades: ").split()
    # Making sure the user enters EXACTLY 14 assignments each of which it within range 0 to 100
    if len(Assignment) != 14 or any(int(i) < 0 for i in Assignment) or any(int(i) > 100 for i in Assignment):
        Assignment = correct_Assign(Assignment)

    # Prompting the user to enter their final grade
    Final = float(input("Enter final grades: "))
    # Making sure the user enters a valid grade (Between 0 and 100)
    if Final < 0 or Final > 100:
        Final = correct_Final(Final)

    # Informing the user that the results are about to be displayed
    print("Your classwork grades are as follows:\n ")
    time_wait(1)

    # Calling the functions that will calculate the grade
    Midterm_Percentage, Quiz_Percentage, Assignment_Percentage, Final_Percentage = \
        classwork_percentage(MT, MT2, Quiz, Assignment, Final)

    # Displaying each individual component of classwork
    print("Midterm percentage: %d%%" % Midterm_Percentage, "out of 30%")  # Midterms percentage
    time_wait(1)

    print("Quizzes percentage: %d%%" % Quiz_Percentage, "out of 15%")  # Quizzes percentage
    time_wait(1)

    print("Assignments percentage: %d%%" % Assignment_Percentage, "out of 15%")  # Assignments percentage
    time_wait(1)

    print("Final percentage: %d%%" % Final_Percentage, "out of 40%")  # Final percentage
    time_wait(2)

    # Asking the user if there is any bonus
    Bonus = input("Is there any bonus?, \"Y\" or \"N\": ")
    # Making sure the user enters a correct response
    if Bonus != "Y" and Bonus != "N":
        Bonus = correct_bonus(Bonus)

    # If there is no bonus given, will set bonus to zero
    if Bonus == "N":
        Grand_bonus = 0
        Assign_per = 0
        Assign_N = 0
        Curve = 0
    else:
        #  If there is bonus given, asking the user for the form of the bonus + its percentage
        time_wait(1)
        Assign_N = int(input("Enter number of assignments: "))
        Assign_per = float(input("Enter each assignment percentage: "))
        Curve = int(input("Enter curve percentage: "))
        # Calculating total bonus given
        Grand_bonus = bonus(Assign_per, Assign_N, Curve)

    # Calling functions that will add the bonus to the final coursework
    Total_Without_Bonus = grand_total(MT, MT2, Quiz, Assignment, Final)
    Total_With_Bonus = Total_Without_Bonus + Grand_bonus
    Grade = grade_letter(MT, MT2, Quiz, Assignment, Final, Assign_per, Assign_N, Curve)

    print("You got: %d%%" % Total_Without_Bonus, "in classwork", "+ %d%% bonus" % Grand_bonus, "so the total is %d%%"
          % Total_With_Bonus, "\nTherefore, your final grade is:", Grade)

    print("To keep a copy of your data,")
    time_wait(1)
    # Asking the user for the name of the file in which they would like to save their data
    file_name = input("Please enter the full path to the file in which you would like to save your data: ")

    # Actual writing process
    file = Write(file_name)
    file.write("Your classwork grades are as follows: ")
    file.write(f"\nMidterm percentage: {Midterm_Percentage}% out of 30%")
    file.write(f"\nQuizzes percentage: {Quiz_Percentage}% out of 15%")
    file.write(f"\nAssignments percentage: {Assignment_Percentage}% out of 15%")
    file.write(f"\nFinal percentage: {Final_Percentage}% out of 40%")
    file.write(f"\nYou got: {Total_Without_Bonus}% in classwork + {Grand_bonus}% so the total is {Total_With_Bonus}%"
               f"\nTherefore, your final grade is {Grade}")
    # Closing the file after finishing the writing process
    file.close()
    # Displaying a message to inform the user that the data has been saved successfully
    print("Data has been saved successfully in",  "\"", file_name, "\"")


else:
    # The user chose whole class statistics
    from Functions_Class_Analysis import*

    print("To display class statistics, you will need to provide the dataset for all grades.")
    time_wait(2)

    # Prompting the user to enter the form in which they will provide the dataset (Terminal, CSV, Excel, Text)
    grades_type = input("Do you have the dataset as plain numbers (directly into terminal) \"1\" "
                        "a CSV file \"2\", an Excel file \"3\", or a text file \"4\": ")

    # Making sure the user enters a correct response
    if grades_type not in ["1", "2", "3", "4"]:
        grades_type = correct_grade_type(grades_type)

    # The user chose to plug the numbers directly into the terminal
    if grades_type == "1":
        # Asking the user to input the grades
        MT = input("Please enter all midterm grades: ").split()  # Enter grades directly into the terminal
        # Making sure the user enters valid grades (Between 0 and 105)
        if any(float(i) < 0 for i in MT) or any(float(i) > 105 for i in MT):
            MT = correct_MT(MT)
        # Graphing the input data
        graph_plain_numbers_or_txt(MT)

    # The user chose to provide the data in the form of a CSV file
    elif grades_type == "2":
        # Asking the user to provide the full path to the CSV file
        file_path = input("Please enter the full path to the csv file: ")  # Provide the full path for the CSV file
        # Making sure the user enters a valid .csv file
        if file_path.lower().endswith(".csv") == False:
            file_path = correct_csv(file_path)

        # Asking the user to enter the header column name for the data (Useful in presence of many columns)
        column_name = input("Please enter column name: ")
        # Extracting data from chosen file/column
        MT = data_csv(file_path, column_name)
        # Graphing the data
        graph_CSV(file_path, column_name)

    # The user chose to provide the data in form of an Excel file
    elif grades_type == "3":
        # Asking the user for the full path for the Excel file
        file_path = input("Enter the full path to xlsx: ")
        # Making sure the user enters a valid .xlsx file
        if file_path.lower().endswith(".xlsx"):
            file_path = correct_xlsx(file_path)

        # Asking the user for the sheet name in which he has the data (Useful in presence of many sheets)
        sheet_name = input("Enter sheet name: ")
        workbook = open_excel(file_path)  # Opening the Excel file in read mode to see its content
        sheet_names = workbook.sheetnames  # Checking what sheets the Excel file has

        # Making sure the entered sheet name actually exists in the Excel file
        if sheet_name in sheet_names:
            # If it exists, the program informs the user that the entered sheet has been found
            print("Sheet found")
        else:
            # Otherwise, if it is not found, the program asks the user to enter a correct sheet name
            sheet_name = correct_sheet_name(sheet_name, file_path)

        # Asking the user for the column name under which is the data
        column_name = input("Enter column name: ")

        # Calling the function that will extract the data from the Excel file
        MT = data_xlsx(file_path, sheet_name, column_name)
        # Calling the graph function
        graph_xlsx(file_path, sheet_name, column_name)

    # The user chose to provide the data in the form of a text file
    else:
        # Asking the user for the path to the text file which has the data
        file_path = input("Enter the full path to the text file: ")
        # Making sure the user enters a valid .txt file
        if file_path.lower().endswith(".txt"):
            file_path = correct_txt(file_path)

        MT = data_txt(file_path)
        graph_plain_numbers_or_txt(MT)

    # Calling the functions that will conduct the statistical analysis on the data
    Number_attendees = No_attendees(MT)  # Number of attendees function
    Average_grade = average(MT)  # Average grade function
    Median = median(MT)  # Median grade function
    Standard_deviation = standard_deviation(MT)  # Standard deviation function
    No_students = No_students_seg(MT)  # Number of students in each grade segment function
    Highest_grade, Lowest_grade = highest_lowest(MT)  # Highest and lowest grade function

    # Displaying the statistics
    print("Number of attendees:", Number_attendees)
    time_wait(1)
    print("The highest grade is:", Highest_grade)
    time_wait(1)
    print("The lowest grade is:", Lowest_grade)
    time_wait(1)
    print("The average grade is:", Average_grade)
    time_wait(1)
    print("The median is:", Median)
    time_wait(1)
    print("The standard deviation is:", Standard_deviation)
    time_wait(1)
    print("Number of students in grade segments [0-5, 5-16, 16-27, 27-38, 38-49, 49-60, 60,71, 71-82, 82-93, 93-104] is:", No_students)
    time_wait(2)

    # Asking the user if they would like to keep a copy of the statistics
    keep_data = input("Would you like to keep a copy of these statistics, yes \"Y\" or no \"N\": ")
    # Making sure the user enters a valid response
    if keep_data != "Y" and keep_data != "N":
        keep_data = correct_YesNo(keep_data)

    if keep_data == "Y":
        # If the user wants to keep a copy of the statistics, the program asks the user for the name of the file to save the data in
        file_name = input("Enter the name of the file in which you would like to save these statistics: ")
        # Calling the write function which will open the file in "write" mode
        file = Write(file_name)

        # The actual data writing process
        file.write("Class statistics are as follows:")
        file.write(f"\nNumber of attendees is: {Number_attendees}")
        file.write(f"\nThe highest grade is: {Highest_grade}\nThe lowest grade is: {Lowest_grade}")
        file.write(f"\nThe average grade is: {Average_grade}")
        file.write(f"\nThe median is: {Median}")
        file.write(f"\nThe standard deviation is: {Standard_deviation}")
        file.write(f"\nNumber of students in grade segments [0-5, 5-16, 16-27, 27-38, 38-49, 49-60, 60,71, 71-82, 82-93, 93-104]"
                   f" is: \n{No_students}")
        # Closing the file after data has been written to it
        file.close()
        # Displaying a message to inform the user that the data has been saved successfully
        print("Data has been saved successfully in",  "\"", file_name, "\"")

    elif keep_data == "N":
        # If the user does not want to keep the statistics, the program prints a farewell message and terminates
        print("Okay, have a nice time.")


