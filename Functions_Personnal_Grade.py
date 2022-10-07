


def correct_MT1(MT):
    # Function to check that the entered midterm1 grade is within correct range [0, 10]
    while MT < 0 or MT > 100:
        MT = float(input("Error! Please, enter correct midterm1 grade: "))
    return MT


def correct_MT2(MT2):
    # Function to check that the entered midterm2 grade is within correct range [0, 100]
    while MT2 < 0 or MT2 > 100:
        MT2 = float(input("Error! Please, enter correct midterm2 grade: "))
    return MT2


def correct_Final(Final):
    # Function to check that the entered final grade is within correct range [0, 100]
    while Final < 0 or Final > 100:
        Final = float(input("Error! Please, enter correct final grade: "))
    return Final


def correct_Quiz(Quiz):
    # Function to check that EXACTLY 5 quizzes are entered AND each of which is within correct range [0, 10]
    list_int(Quiz)

    while len(Quiz) != 5 or any(i < 0 for i in Quiz) or any(i > 10 for i in Quiz):
        if len(Quiz) != 5:
            while len(Quiz) != 5:
                Quiz = input("Error! Please, enter EXACTLY 5 quiz grades: ").split()
                list_int(Quiz)

        while any(i < 0 for i in Quiz) or any(i > 10 for i in Quiz):
            Quiz = input("Error! Please, enter your 5 quiz grades correctly: ").split()
            list_int(Quiz)
    return Quiz


def correct_Assign(Assignment):
    # Function to check that EXACTLY 14 assignments are entered AND each of which is within correct range [0, 100]
    list_int(Assignment)

    while len(Assignment) != 14 or any(i < 0 for i in Assignment) or any(i > 100 for i in Assignment):
        if len(Assignment) != 14:
            while len(Assignment) != 14:
                Assignment = input("Error! Please, enter EXACTLY 14 assignment grades: ").split()
                list_int(Assignment)

        while any(i < 0 for i in Assignment) or any(i > 100 for i in Assignment):
            Assignment = input("Error! Please, enter your 14 assignment grades correctly: ").split()
            list_int(Assignment)
    return Assignment


def list_int(List):
    # Function to convert from string value of elements in a list to their numerical values
    for i in range(len(List)):
        List[i] = int(List[i])


def sort(List):
    # Function to sort list numbers in descending order
    list_int(List)

    for i in range(len(List)):
        for j in range(i+1, len(List)):
            if List[i] < List[j]:
                tmp1 = List[i]
                List[i] = List[j]
                List[j] = tmp1
    List_sorted = List
    return List_sorted


def mid_grade(MT, MT2):
    # Function to calculate the total grade of midterms 1 and 2 using 40% 60% policy
    if MT >= MT2:
        MT = MT * 60/100
        MT2 = MT2 * 40/100
        Mid_Grade = (MT + MT2) * 30/100
        return Mid_Grade

    else:
        MT2 = MT2 * 60/100
        MT = MT * 40/100
        Mid_Grade = (MT + MT2) * 30/100
        return Mid_Grade

def quiz_grade(Quiz):
    # Function to calculate the total grade of the best four out of five quizzes
    sort(Quiz)
    Best_4 = Quiz[0:4]
    Sum = 0

    for i in range(len(Best_4)):
        Sum = Sum + Best_4[i]
    Quiz_Grade = Sum / 40 * 15/100 * 100
    return Quiz_Grade


def assign_grade(Assignment):
    # Function to calculate the total grade of best 12 assignments out of 14
    sort(Assignment)
    Best_12 = Assignment[0:12]
    Sum = 0

    for i in range(len(Best_12)):
        Sum = Sum + Assignment[i]
    Assign_Grade = round(Sum / 1200 * 15/100 * 100, 2)
    return Assign_Grade


def final_grade(Final):
    # Function to calculate the grade of the final exam
    Final_Grade = round(Final * 40/100, 2)
    return Final_Grade


def correct_bonus(Bonus):
    # Function to check that the entered answer to bonus question is correct ("Y" or "N")
    while Bonus != "Y" and Bonus != "N":
        Bonus = input("Error! Please, enter \"Y\" or \"N\" : ")
    return Bonus


def bonus(Assign_per, Assign_N, Curve):
    # Function to calculate the amount of bonus given
    Grand_bonus = (Assign_per * Assign_N) + Curve
    return Grand_bonus


def grand_total(MT, MT2, Quiz, Assignment, Final):
    # Function to calculate the total coursework percentage of a student
    quiz = quiz_grade(Quiz)
    mid = mid_grade(MT, MT2)
    assign = assign_grade(Assignment)
    final = final_grade(Final)

    Total = quiz + mid + assign + final
    return Total


def grade_letter(MT, MT2, Quiz, Assignment, Final, Assign_per, Assign_N, Curve):
    # Function to print the final letter grade of the course
    Grand_bonus = bonus(Assign_per, Assign_N, Curve)
    Total_Without_Bonus = grand_total(MT, MT2, Quiz, Assignment, Final)
    Total_With_Bonus = Total_Without_Bonus + Grand_bonus

    if Total_With_Bonus >= 95 and Total_With_Bonus <= 100:
        Grade = "A"
    elif Total_With_Bonus >= 90 and Total_With_Bonus < 95:
        Grade = "A-"
    elif Total_With_Bonus >= 85 and Total_With_Bonus < 90:
        Grade = "B+"
    elif Total_With_Bonus >= 80 and Total_With_Bonus < 85:
        Grade = "B"
    elif Total_With_Bonus >= 75 and Total_With_Bonus < 80:
        Grade = "B-"
    elif Total_With_Bonus >= 70 and Total_With_Bonus < 75:
        Grade = "C+"
    elif Total_With_Bonus >= 65 and Total_With_Bonus < 70:
        Grade = "C"
    elif Total_With_Bonus >= 60 and Total_With_Bonus < 65:
        Grade = "C-"
    else:
        Grade = "F"
    return Grade


def classwork_percentage(MT, MT2, Quiz, Assignment, Final):
    # Function to determine the percentage grade of each component of classwork
    Midterm_Percentage = mid_grade(MT, MT2)
    Quiz_Percentage = quiz_grade(Quiz)
    Assignment_Percentage = assign_grade(Assignment)
    Final_Percentage = final_grade(Final)
    return Midterm_Percentage, Quiz_Percentage, Assignment_Percentage, Final_Percentage


def time_wait(n):
    # Functon to halt the execution of the program for a specific time interval
    import time
    time.sleep(n)


def Write(file_name):
    # Function to write the output into a new file
    Write = open(file_name, "w")
    return Write



