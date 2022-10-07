import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *
import numpy as np


class Ui_Main_Personal_Grade(object):
    def setupUi(self, Main_Personal_Grade):

        Validator = QRegExpValidator(QRegExp(r'[0-9- -.]+'))

        Main_Personal_Grade.setObjectName("Main_Personal_Grade")
        Main_Personal_Grade.resize(760, 506)
        self.centralwidget = QtWidgets.QWidget(Main_Personal_Grade)
        self.centralwidget.setObjectName("centralwidget")
        self.Mid_1_Grade_label = QtWidgets.QLabel(self.centralwidget)
        self.Mid_1_Grade_label.setGeometry(QtCore.QRect(20, 10, 140, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Mid_1_Grade_label.setFont(font)
        self.Mid_1_Grade_label.setObjectName("Mid_1_Grade_label")
        self.Mid_2_Grade_label = QtWidgets.QLabel(self.centralwidget)
        self.Mid_2_Grade_label.setGeometry(QtCore.QRect(20, 50, 140, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Mid_2_Grade_label.setFont(font)
        self.Mid_2_Grade_label.setObjectName("Mid_2_Grade_label")
        self.Enter_Final_label = QtWidgets.QLabel(self.centralwidget)
        self.Enter_Final_label.setGeometry(QtCore.QRect(20, 170, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Enter_Final_label.setFont(font)
        self.Enter_Final_label.setObjectName("Enter_Final_label")
        self.Enter_5_Q_label = QtWidgets.QLabel(self.centralwidget)
        self.Enter_5_Q_label.setGeometry(QtCore.QRect(20, 90, 140, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Enter_5_Q_label.setFont(font)
        self.Enter_5_Q_label.setObjectName("Enter_5_Q_label")
        self.Enter_14_Assignment_label = QtWidgets.QLabel(self.centralwidget)
        self.Enter_14_Assignment_label.setGeometry(QtCore.QRect(20, 130, 160, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Enter_14_Assignment_label.setFont(font)
        self.Enter_14_Assignment_label.setObjectName("Enter_14_Assignment_label")
        ###
        self.lineEdit_MT_1 = QtWidgets.QLineEdit(self.centralwidget)
        ###
        self.lineEdit_MT_1.setValidator(Validator)
        self.lineEdit_MT_1.setGeometry(QtCore.QRect(160, 10, 161, 31))
        self.lineEdit_MT_1.setObjectName("lineEdit_MT_1")
        ###
        self.lineEdit_MT1_2 = QtWidgets.QLineEdit(self.centralwidget)
        ###
        self.lineEdit_MT1_2.setValidator(Validator)
        self.lineEdit_MT1_2.setGeometry(QtCore.QRect(160, 50, 161, 31))
        self.lineEdit_MT1_2.setObjectName("lineEdit_MT1_2")
        ###
        self.lineEdit_5_Quizzes = QtWidgets.QLineEdit(self.centralwidget)
        ###
        self.lineEdit_5_Quizzes.setValidator(Validator)
        self.lineEdit_5_Quizzes.setGeometry(QtCore.QRect(160, 100, 281, 31))
        self.lineEdit_5_Quizzes.setObjectName("lineEdit_5_Quizzes")
        ###
        self.lineEdit_14_Assignment = QtWidgets.QLineEdit(self.centralwidget)
        ###
        self.lineEdit_14_Assignment.setValidator(Validator)
        self.lineEdit_14_Assignment.setGeometry(QtCore.QRect(180, 140, 481, 31))
        self.lineEdit_14_Assignment.setObjectName("lineEdit_14_Assignment")
        ###
        self.lineEdit_Final = QtWidgets.QLineEdit(self.centralwidget)
        ###
        self.lineEdit_Final.setValidator(Validator)
        self.lineEdit_Final.setGeometry(QtCore.QRect(160, 180, 211, 31))
        self.lineEdit_Final.setObjectName("lineEdit_Final")
        #####
        self.pushButton_MT1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.correct_MT1())
        #####
        self.pushButton_MT1.setGeometry(QtCore.QRect(370, 10, 81, 31))
        self.pushButton_MT1.setObjectName("pushButton_MT1")
        #####
        self.pushButton_MT2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.correct_MT2())
        #####
        self.pushButton_MT2.setGeometry(QtCore.QRect(370, 50, 81, 31))
        self.pushButton_MT2.setObjectName("pushButton_MT2")
        #####
        self.pushButton_Quizzes = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.correct_Quiz())
        #####
        self.pushButton_Quizzes.setGeometry(QtCore.QRect(480, 100, 81, 31))
        self.pushButton_Quizzes.setObjectName("pushButton_Quizzes")
        #####
        self.pushButton_Assignment = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.correct_Assign())
        #####
        self.pushButton_Assignment.setGeometry(QtCore.QRect(670, 140, 81, 31))
        self.pushButton_Assignment.setObjectName("pushButton_Assignment")
        #####
        self.pushButton_Final = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.correct_Final())
        #####
        self.pushButton_Final.setGeometry(QtCore.QRect(400, 180, 81, 31))
        self.pushButton_Final.setObjectName("pushButton_Final")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 220, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        #####
        self.pushButton_YES_Bonus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.YES_bonus())
        #####
        self.pushButton_YES_Bonus.setGeometry(QtCore.QRect(200, 220, 111, 41))
        self.pushButton_YES_Bonus.setObjectName("pushButton_YES_Bonus")
        #####
        self.pushButton_NO_Bonus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.NO_bonus())
        #####
        self.pushButton_NO_Bonus.setGeometry(QtCore.QRect(350, 220, 111, 41))
        self.pushButton_NO_Bonus.setObjectName("pushButton_NO_Bonus")
        self.Number_of_assignment_label = QtWidgets.QLabel(self.centralwidget)
        self.Number_of_assignment_label.setGeometry(QtCore.QRect(20, 280, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Number_of_assignment_label.setFont(font)
        self.Number_of_assignment_label.setObjectName("Number_of_assignment_label")
        ###
        self.No_assignment_percentage = QtWidgets.QLineEdit(self.centralwidget)
        ###
        self.No_assignment_percentage.setValidator(Validator)
        self.No_assignment_percentage.setGeometry(QtCore.QRect(200, 280, 141, 31))
        self.No_assignment_percentage.setObjectName("No_assignment_percentage")
        self.percentage_of_assignment_label = QtWidgets.QLabel(self.centralwidget)
        self.percentage_of_assignment_label.setGeometry(QtCore.QRect(380, 280, 185, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.percentage_of_assignment_label.setFont(font)
        self.percentage_of_assignment_label.setObjectName("percentage_of_assignment_label")
        ###
        self.Percentage_Bonus_assignment = QtWidgets.QLineEdit(self.centralwidget)
        ###
        self.Percentage_Bonus_assignment.setValidator(Validator)
        self.Percentage_Bonus_assignment.setGeometry(QtCore.QRect(570, 280, 141, 31))
        self.Percentage_Bonus_assignment.setObjectName("Percentage_Bonus_assignment")
        self.Curve_percentage_label = QtWidgets.QLabel(self.centralwidget)
        self.Curve_percentage_label.setGeometry(QtCore.QRect(20, 330, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Curve_percentage_label.setFont(font)
        self.Curve_percentage_label.setObjectName("Curve_percentage_label")
        ###
        self.Curve_percentage_line = QtWidgets.QLineEdit(self.centralwidget)
        ###
        self.Curve_percentage_line.setValidator(Validator)
        self.Curve_percentage_line.setGeometry(QtCore.QRect(170, 330, 141, 31))
        self.Curve_percentage_line.setObjectName("Curve_percentage_line")
        self.pushButton_calculate = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.grand_total())
        self.pushButton_calculate.setGeometry(QtCore.QRect(190, 380, 351, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_calculate.setFont(font)
        self.pushButton_calculate.setAutoFillBackground(False)
        self.pushButton_calculate.setStyleSheet("")
        self.pushButton_calculate.setObjectName("pushButton")
        Main_Personal_Grade.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main_Personal_Grade)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 21))
        self.menubar.setObjectName("menubar")
        Main_Personal_Grade.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main_Personal_Grade)
        self.statusbar.setObjectName("statusbar")
        Main_Personal_Grade.setStatusBar(self.statusbar)

        self.retranslateUi(Main_Personal_Grade)
        QtCore.QMetaObject.connectSlotsByName(Main_Personal_Grade)

    def retranslateUi(self, Main_Personal_Grade):
        _translate = QtCore.QCoreApplication.translate
        Main_Personal_Grade.setWindowTitle(_translate("Main_Personal_Grade", "MainWindow"))
        self.Mid_1_Grade_label.setText(_translate("Main_Personal_Grade", "Mid term 1 Grade:"))
        self.Mid_2_Grade_label.setText(_translate("Main_Personal_Grade", "Mid term 2 Grade:"))
        self.Enter_Final_label.setText(_translate("Main_Personal_Grade", "Enter Final Grade:"))
        self.Enter_5_Q_label.setText(_translate("Main_Personal_Grade", "Enter 5 Quizzes:"))
        self.Enter_14_Assignment_label.setText(_translate("Main_Personal_Grade", "Enter 14 Assignment:"))
        self.pushButton_MT1.setText(_translate("Main_Personal_Grade", "Check"))
        self.pushButton_MT2.setText(_translate("Main_Personal_Grade", "Check"))
        self.pushButton_Quizzes.setText(_translate("Main_Personal_Grade", "Check"))
        self.pushButton_Assignment.setText(_translate("Main_Personal_Grade", "Check"))
        self.pushButton_Final.setText(_translate("Main_Personal_Grade", "Check"))
        self.label.setText(_translate("Main_Personal_Grade", "Is there any bonus?"))
        self.pushButton_YES_Bonus.setText(_translate("Main_Personal_Grade", "YES"))
        self.pushButton_NO_Bonus.setText(_translate("Main_Personal_Grade", "NO"))
        self.Number_of_assignment_label.setText(_translate("Main_Personal_Grade", "Number of Assignment:"))
        self.percentage_of_assignment_label.setText(_translate("Main_Personal_Grade", "Assignment Percentage:"))
        self.Curve_percentage_label.setText(_translate("Main_Personal_Grade", "Curve Percentage:"))
        self.pushButton_calculate.setText(_translate("Main_Personal_Grade", "Calculate"))



    ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

    def showErrorMsg(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(text)
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()



    def correct_MT1(self):
        # Function to check that the entered midterm1 grade is within correct range [0, 100]
        try:
            MT1_grade = float(self.lineEdit_MT_1.text())
            if (MT1_grade < 0 or MT1_grade > 100):
                raise Exception
            else:
                self.MT1 = MT1_grade

        except:
            self.showErrorMsg("Invalid value")



    def correct_MT2(self):
        # Function to check that the entered midterm2 grade is within correct range [0, 100]

        try:
            MT2_grade = float(self.lineEdit_MT1_2.text())
            if (MT2_grade < 0 or MT2_grade > 100):
                raise Exception
            else:
                self.MT2 = MT2_grade

        except:
            self.showErrorMsg("Invalid value")



    def correct_Quiz(self):
        # Function to check that EXACTLY 5 quizzes are entered AND each of which is within correct range [0, 10]
        try:
            self.Quizs= (self.lineEdit_5_Quizzes.text()).split()
            if len(self.Quizs) != 5 or any(int(i) < 0 for i in self.Quizs) or any(int(i) > 10 for i in self.Quizs):
                    raise Exception
            else:
                self.Quiz_Grade = self.Quizs

        except:
           self.showErrorMsg("Invalid value")


    def correct_Assign(self):
        # Function to check that EXACTLY 14 assignments are entered AND each of which is within correct range [0, 100]
        try:
            Assignment=  (self.lineEdit_14_Assignment.text()).split()

            if len(Assignment) != 14 or any(int(i) < 0 for i in Assignment) or any(int(i) > 100 for i in Assignment):
                raise Exception
            else:
                self.assignment_grade = Assignment

        except:
            self.showErrorMsg("Invalid value")




    def correct_Final(self):
        # Function to check that the entered final grade is within correct range [0, 100]
        try:
            Final = float(self.lineEdit_Final.text())
            if  Final < 0 or Final > 100:
                raise Exception
            else:
                self.Final_Grade = Final

        except:
            self.showErrorMsg("Invalid value")



#=================================================================================================================================================================
    def sort(self, list):
        # Function to sort list numbers in descending order
        for i in range(len(list)):
            for j in range(i+1, len(list)):
                if int(list[i]) < int(list[j]):
                    tmp1 = list[i]
                    list[i] = list[j]
                    list[j] = tmp1
        return list



    def mid_grade(self):
        # Function to calculate the total grade of midterms 1 and 2 using 40% 60% policy
        if self.MT1 > self.MT2:
            self.MT1 = self.MT1 * 60/100
            self.MT2 = self.MT2 * 40/100
            self.Mid_Grade = (self.MT1 + self.MT2) * 30/100
            return self.Mid_Grade
        else:
            self.MT2 = self.MT2 * 60/100
            self.MT1 = self.MT1 * 40/100
            self.Mid_Grade = (self.MT1 + self.MT2) * 30/100



    def quiz_grade(self):
        # Function to calculate the total grade of the best four out of five quizzes

        self.Quiz_Grade= self.sort(self.Quiz_Grade)
        self.Best_4 = self.Quiz_Grade[0:4]
        self.Sum = 0

        for i in range(len(self.Best_4)):
            self.Sum = self.Sum + float(self.Best_4[i])
        self.Quiz_Grade =self.Sum / 40 * 15/100 * 100


    def assign_grade(self):
        # Function to calculate the total grade of best 12 assignments out of 14
        self.sort(self.assignment_grade)
        self.Best_12 = self.assignment_grade[0:12]
        self.Sum = 0

        for i in range(len(self.Best_12)):
            self.Sum = self.Sum + float(self.assignment_grade[i])
        self.Assign_Grade = round(self.Sum / 1200 * 15/100 * 100, 2)


    def final_grade(self):
        # Function to calculate the grade of the final exam
        self.Final_Grade = round(self.Final_Grade * 40/100, 2)

    def YES_bonus(self):
        self.No_assignment_percentage.setVisible(True)
        self.Percentage_Bonus_assignment.setVisible(True)
        self.Curve_percentage_line.setVisible(True)
        self.Number_of_assignment_label.setVisible(True)
        self.percentage_of_assignment_label.setVisible(True)
        self.Curve_percentage_label.setVisible(True)


    def NO_bonus(self):
        self.No_assignment_percentage.setText('0')
        self.Percentage_Bonus_assignment.setText('0')
        self.Curve_percentage_line.setText('0')
        self.No_assignment_percentage.setVisible(False)
        self.Percentage_Bonus_assignment.setVisible(False)
        self.Curve_percentage_line.setVisible(False)
        self.Number_of_assignment_label.setVisible(False)
        self.percentage_of_assignment_label.setVisible(False)
        self.Curve_percentage_label.setVisible(False)


    def grand_total(self):
        # Function to calculate the total coursework percentage of a student
        try:
            self.num_assignment = float(self.No_assignment_percentage.text())

            if self.num_assignment < 0:
                raise Exception

            self.Percentage_Bonus_assignment_value = float(self.Percentage_Bonus_assignment.text())

            if self.Percentage_Bonus_assignment_value < 0:
                raise Exception

            self.Curve_percentage_line_value = float(self.Curve_percentage_line.text())

            if self.Curve_percentage_line_value < 0:
                raise Exception

            self.correct_Assign()
            self.assign_grade()
            self.mid_grade()
            self.correct_Quiz()
            self.quiz_grade()
            self.final_grade()


            self.bouns = self.Curve_percentage_line_value + (
                        self.num_assignment * self.Percentage_Bonus_assignment_value)

            self.Total_Without_Bonus = self.Quiz_Grade + self.Mid_Grade + self.Assign_Grade + self.Final_Grade
            self.Total_With_Bonus = self.Total_Without_Bonus + self.bouns

            self.grade_letter()
            self.showErrorMsg(str(self.Total_With_Bonus) + " % " + self.Grade)


            self.file = open("Personal_Grade.txt", "w+")
            self.file.write("Your classwork grades are as follows: ")

            self.file.write(f"\nMidterm percentage: {self.Mid_Grade}% out of 30%")
            self.file.write(f"\nQuizzes percentage: {self.Quiz_Grade}% out of 15%")
            self.file.write(f"\nAssignments percentage: {self.Assign_Grade}% out of 15%")
            self.file.write(f"\nFinal percentage: {self.Final_Grade}% out of 40%")
            self.file.write(
                f"\nYou got: {self.Total_Without_Bonus}% in classwork + {self.bouns}% so the total is {self.Total_With_Bonus}%"
                f"\nTherefore, your final grade is {self.Grade}")
            self.file.close()

        except Exception as e:
            self.showErrorMsg("Invalid value")
            print(e)






    def grade_letter(self):
        # Function to print the final letter grade of the course


        if self.Total_With_Bonus >= 95 and self.Total_With_Bonus <= 100:
            self.Grade = "A"
        elif self.Total_With_Bonus >= 90 and self.Total_With_Bonus < 95:
            self.Grade = "A-"
        elif self.Total_With_Bonus >= 85 and self.Total_With_Bonus < 90:
            self.Grade = "B+"
        elif self.Total_With_Bonus >= 80 and self.Total_With_Bonus < 85:
            self.Grade = "B"
        elif self.Total_With_Bonus >= 75 and self.Total_With_Bonus < 80:
            self.Grade = "B-"
        elif self.Total_With_Bonus >= 70 and self.Total_With_Bonus < 75:
            self.Grade = "C+"
        elif self.Total_With_Bonus >= 65 and self.Total_With_Bonus < 70:
            self.Grade = "C"
        elif self.Total_With_Bonus >= 60 and self.Total_With_Bonus < 65:
            self.Grade = "C-"
        else:
            self.Grade = "F"



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_Personal_Grade = QtWidgets.QMainWindow()
    ui = Ui_Main_Personal_Grade()
    ui.setupUi(Main_Personal_Grade)
    Main_Personal_Grade.show()
    sys.exit(app.exec_())
