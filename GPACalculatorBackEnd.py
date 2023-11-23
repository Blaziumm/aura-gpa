#tkiner is used for GUI
import math

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
#Will store the list of our grades.
gradeDictionary = []

#Convers a letter grade and level into the value assigned at the start
def gradeTranslator(grade, Level):
    #Input is already validated so we can only check the 5 options
    #Checks what level the class is so we can look up the right value
    #standard level
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
    #Honors Level
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
    #AP level
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
#Grade list is created by the software, so we do not have to validate it.
def GPACalculator(gradelist, weighted):
    #Creates a varible to store the total of all the credits from the grade.
    gradetotal = 0
    #If we do not have any classes and grades, return 0
    if len(gradelist) == 0:
        return(0)
    #If we do have data
    else:
        #if we are not calculating the weighted GPA
        if weighted == False:
            for i in range(len(gradelist)):
                #Add the point value of each grade to our running total of scores with a "Standard" Class level as
                #We are calculating the non-weighted GPA.
                gradetotal += gradeTranslator(gradelist[i][1], 0)
        else:
            for i in range(len(gradelist)):
                #Add the point value of each grade to our running total of scores with the actual class level
                gradetotal = gradetotal + gradeTranslator(gradelist[i][1], int(gradelist[i][2]))
                
        #Returns the average of the grades
        return(gradetotal/len(gradelist))  

#Takes in a number between 100 and 0, and calculates the letter grade based off the grade values we set.
def numbergradetoletter(grade):
    try:
        print(round(grade))
        intgrade = round(grade)
        if intgrade < 101 and intgrade > -1:
            if intgrade > scoreRequiredforA or intgrade == scoreRequiredforA:
                return("A")
            elif intgrade >scoreRequiredforB or intgrade == scoreRequiredforB:
                return("B")
            elif intgrade >scoreRequiredforC or intgrade == scoreRequiredforC:
                return("C")
            elif intgrade >scoreRequiredforD or intgrade == scoreRequiredforD:
                return("D")
            elif intgrade  < scoreRequiredforD:
                return("E")
            else: 
                return("NUMOUT OF RANGE")
    except ValueError or TypeError:
        if grade == "A" or grade == "B" or grade == "C" or grade == "D" or grade == "E":
            return(grade)
        else: 
            return("OUT OF RANGE")

#Appends a grade to the gradeDictionary.
def addGrade(name, grade, level):
    gradeDictionary.append([name, numbergradetoletter(grade), level])


def round(num):
    num = float(num)
    if num > math.floor(num) + 0.5 or num == math.floor(num) + 0.5:
        return(math.ceil(num))
    else:
        return(math.floor(num))

