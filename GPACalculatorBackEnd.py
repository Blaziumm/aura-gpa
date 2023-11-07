#tkiner is used for GUI
import tkinter as tk
import tkinter.font as tkFont

#Toggles Terminal Only Mode
terminalMode = True



#List of the letter grade values for each level of class,
#Goes from A-E in that order
standardlist = [4, 3, 2, 1, 0]
honorlist = [4.5, 3.5, 2.5, 1.5, 0.5]
aplist = [5, 4, 3, 2, 1]

#Designates what the required score is for each letter grade
scoreRequiredforA = 90
scoreRequiredforB = 80
scoreRequiredforC = 70
scoreRequiredforD = 60
scoreRequiredforE = 50


#Internal Values
exitnotrequested = True
##Will store the list of our grades.
gradeDictionary = []
##Set a list of classes for easy printing
classes = ""

#Convers a letter grade and level into the value assigned at the start
def gradeTranslator(grade, Level):
    if Level == 0:
        if grade == "A":
            return(standardlist[0])
        elif grade == "B":
            return(standardlist[1])
        elif grade == "C":
            return(standardlist[2])
        elif grade == "D":
            return(standardlist[3])
        elif grade == "E":
            return(standardlist[4])           
    elif Level == 1:
        if grade == "A":
            return(honorlist[0])
        elif grade == "B":
            return(honorlist[1])
        elif grade == "C":
            return(honorlist[2])
        elif grade == "D":
            return(honorlist[3])
        elif grade == "E":
            return(honorlist[4])     
    elif Level == 2:
        if grade == "A":
            return(aplist[0])
        elif grade == "B":
            return(aplist[1])
        elif grade == "C":
            return(aplist[2])
        elif grade == "D":
            return(aplist[3])
        elif grade == "E":
            return(aplist[4])    

#Calculates the GPA, takes in a 2D list with the grades and names, and a boolean value of if we are calculating weighted
#GPA or unweighted
def GPACalculator(gradelist, weighted):
    gradetotal = 0
    if len(gradelist) == 0:
        return(0)
    else:
        if weighted == False:
            for i in range(len(gradelist)):
                gradetotal += gradeTranslator(gradelist[i][1], 0)
            return(gradetotal/len(gradelist)) 
        else:
            for i in range(len(gradelist)):
                gradetotal = gradetotal + gradeTranslator(gradelist[i][1], int(gradelist[i][2]))
            return(gradetotal/len(gradelist))  

#Takes in a number between 100 and 0, and calculates the letter grade based off the grade values we set.
def numbergradetoletter(grade):
    try:
        intgrade = int(grade)
        if intgrade < 101 and intgrade > -1:
            if intgrade > scoreRequiredforA or intgrade == scoreRequiredforA:
                return("A")
            elif intgrade >scoreRequiredforB or intgrade == scoreRequiredforB:
                return("B")
            elif intgrade >scoreRequiredforC or intgrade == scoreRequiredforC:
                return("C")
            elif intgrade >scoreRequiredforD or intgrade == scoreRequiredforD:
                return("D")
            elif intgrade >scoreRequiredforE or intgrade == scoreRequiredforE:
                return("E")
            else: 
                return("OUT OF RANGE")
    except:
        if grade == "A" or grade == "B" or grade == "C" or grade == "D" or grade == "E":
            return(grade)
        else: 
            return("OUT OF RANGE")

#Appends a grade to the gradeDictionary.
def addGrade(name, grade, level):
    gradeDictionary.append([name, numbergradetoletter(grade), level])

