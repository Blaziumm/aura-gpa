import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from GPACalculatorBackEnd import *
import time as time

levelList = []
classInstancelist = []
ErrorList = []

nameAndGradelist = []
adjustedbottomy = 0
amountofclasses = 0
xshift = 70


class App:
    def __init__(self, root):
        global labelList, entryList, buttonList
        labelList = []
        entryList = []
        buttonList = []
        
        #setting title
        root.title("GPA Calculator")
        #setting window size
        width=700
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        filename = PhotoImage(file = "backround.png")
        background_label = Label(root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = filename

        ft = tkFont.Font(family='Dosis',size=10)
        CalculateButton=tk.Button(root)
        CalculateButton["anchor"] = "center"
        CalculateButton["bg"] = "#ffffff"
        CalculateButton["font"] = ft
        CalculateButton["fg"] = "#010005"
        CalculateButton["justify"] = "center"
        CalculateButton["text"] = "Calculate"
        CalculateButton["relief"] = "raised"
        CalculateButton.place(x=245,y=463,width=125,height=25)
        CalculateButton["command"] = CalculateGPA

        AddButton=tk.Button(root)
        AddButton["anchor"] = "center"
        AddButton["bg"] = "#f0f0f0"
        AddButton["font"] = ft
        AddButton["fg"] = "#000000"
        AddButton["justify"] = "center"
        AddButton["text"] = "Add Class"
        AddButton["relief"] = "raised"
        AddButton.place(x=415,y=463,width=125,height=25)
        AddButton["command"] = AddButtoncalled

        # Create A Button
        settingsimg = PhotoImage(file = "SettingsButton.png")
        settings=tk.Button(root, image = settingsimg, border = 0)
        settings["anchor"] = "center"
        settings["justify"] = "center"
        settings["relief"] = "raised"
        settings["image"] = settingsimg
        settings.place(x=20,y=455,width=30, height=30)
        settings["command"] = TMPCALLBACK
        settings.image = settingsimg

def classmaker(root):
        global amountofclasses, AddGradeEntry, AddClassNameEntry, xshift, buttonList

        amountofclasses = amountofclasses + 1

        if amountofclasses == 9:
            Error = Label(root, text = "Maximum Amount Of Classes Added (8)", fg = "red", font = ("Dosis", 12))
            Error.place(x=245,y=430)
            amountofclasses == 10
            
        elif amountofclasses == 10:
             pass
        
        else:
            adjustedbottomy = 50 + amountofclasses * 40
            if amountofclasses == 1:
                ist1 = addclass(root, amountofclasses, adjustedbottomy)
                classInstancelist.append(ist1)

            elif amountofclasses == 2:
                ist2 = addclass(root, amountofclasses, adjustedbottomy)
                classInstancelist.append(ist2)

            elif amountofclasses == 3:
                ist3 = addclass(root, amountofclasses, adjustedbottomy)
                classInstancelist.append(ist3)

            elif amountofclasses == 4:
                ist4 = addclass(root, amountofclasses, adjustedbottomy)
                classInstancelist.append(ist4)
            
            elif amountofclasses == 5:
                ist5 = addclass(root, amountofclasses, adjustedbottomy)
                classInstancelist.append(ist5)

            elif amountofclasses == 6:
                ist6 = addclass(root, amountofclasses, adjustedbottomy)
                classInstancelist.append(ist6)

            elif amountofclasses == 7:
                ist7 = addclass(root, amountofclasses, adjustedbottomy)
                classInstancelist.append(ist7)
            elif amountofclasses == 8:
                ist8 = addclass(root, amountofclasses, adjustedbottomy)
                classInstancelist.append(ist8)

class addclass:
  
    def __init__(self, root, instancenum, adjustedbottomy):
        self.instancenum = instancenum
        self.id = "Entry" + " " + str(amountofclasses)
        ft = tkFont.Font(family='Dosis',size=10)

        self.canvas = Canvas(root).place(x=533,y=adjustedbottomy,width=35,height=30)

        self.buttonvar = IntVar()
        self.buttonoutput = 0

        self.standardbutton = Radiobutton(self.canvas, indicatoron=0, text="S", variable= self.buttonvar, font='Dosis, 10', value=0, command = lambda n=0: self.setvar(n)).place(x=533,y=adjustedbottomy,width=35,height=30)
        self.honorsbutton = Radiobutton(self.canvas, indicatoron=0, text="H", variable= self.buttonvar, font='Dosis, 10', value=1, command = lambda n=1: self.setvar(n)).place(x=573,y=adjustedbottomy,width=35,height=30)
        self.apbutton = Radiobutton(self.canvas, indicatoron=0, text="AP", variable= self.buttonvar, font='Dosis, 10', value=2, command =lambda n=2: self.setvar(n)).place(x=613,y=adjustedbottomy,width=35,height=30)

        AddClassNameEntry=tk.Entry(root)
        AddClassNameEntry["borderwidth"] = "1px"
        AddClassNameEntry["font"] = ft
        AddClassNameEntry["fg"] = "#140a1f"
        AddClassNameEntry["justify"] = "center"
        AddClassNameEntry["text"] = "Class" + self.id
        AddClassNameEntry.place(x=185,y=adjustedbottomy,width=130,height=30)
        AddGradeEntry=tk.Entry(root)
        AddGradeEntry["borderwidth"] = "1px"
        AddGradeEntry["font"] = ft
        AddGradeEntry["fg"] = "#140a1f"
        AddGradeEntry["justify"] = "center"
        AddGradeEntry["text"] = "Grade" + self.id
        AddGradeEntry.place(x=355,y=adjustedbottomy,width=130,height=30)
        entryList.append(AddClassNameEntry)
        entryList.append(AddGradeEntry)
    
    def setvar(self, n):
        self.buttonoutput = n

def AddButtoncalled():
    classmaker(root)

def CalculateGPA():
        global AddGradeEntry, AddClassNameEntry
        gradeDictionary.clear()
        nameAndGradelist.clear()
        levelList.clear()

        for i in range(int(len(entryList))):
            if i % 2 > 0:
                pass
            else:
                className = str(entryList[i].get())
                classGrade = entryList[i+1].get()
                nameAndGradelist.append([className, classGrade])
        
        for i in range(len(classInstancelist)):
            levelList.append(classInstancelist[i].buttonoutput)
        
        for i in range(len(levelList)):
            addGrade(nameAndGradelist[i][0], nameAndGradelist[i][1].upper(), levelList[i])
                
        print(gradeDictionary)
        try:
            Error = Label().destroy
            Error = Label(root, text = "GPA: " + str(GPACalculator(gradeDictionary, True)), fg = "White", font = ("Dosis", 12), bg= "#010005")
            Error.pack(side=BOTTOM, pady= 45)
            
        except:
            Error = Label(root, text = "GPA of 0 or an Error Has Occured", fg = "RED", font = ("Dosis", 12), bg= "#010005")
            Error.pack(side=BOTTOM, pady= 45)
            ErrorList.append(Error)

def TMPCALLBACK():
     print("ahh")

if __name__ == "__main__":
    global root
    root = tk.Tk()
    app = App(root)
    classmaker(root)

    root.mainloop()
