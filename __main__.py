import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from GPACalculatorBackEnd import *

levellst = []
amountofclasses = 0
xshift = 70
adjustedbottomy = 0
classlist = []
NameandGradelist = []

class App:
    def __init__(self, root):
        global GradeEntry, ClassNameEntry, lbllst, newRowFrame, entlst, butlst
        lbllst = []
        entlst = []
        butlst = []
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


        

        ft = tkFont.Font(family='Times',size=10)
        CalculateButton=tk.Button(root)
        CalculateButton["anchor"] = "center"
        CalculateButton["bg"] = "#ffffff"
        CalculateButton["font"] = ft
        CalculateButton["fg"] = "#010005"
        CalculateButton["justify"] = "center"
        CalculateButton["text"] = "Calculate"
        CalculateButton["relief"] = "raised"
        CalculateButton.place(x=245,y=463,width=125,height=25)
        CalculateButton["command"] = GButton_374_command

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
        settings["command"] = pritn
        settings.image = settingsimg
        


def classmaker(root):
        global amountofclasses, AddGradeEntry, AddClassNameEntry, xshift, butlst
        

        if amountofclasses == 8:
            Error = Label(root, text = "Maximum Amount Of Classes Added", fg = "red", font = ("Helvetica", 12))
            Error.place(x=245,y=430)
            amountofclasses == 404
        elif amountofclasses == 404:
             pass
        else:
            amountofclasses = amountofclasses + 1
            adjustedbottomy = 90 + amountofclasses * 40
            if amountofclasses == 1:
                ist1 = addclass(root, amountofclasses, adjustedbottomy)
                classlist.append(ist1)
            elif amountofclasses == 2:
                ist2 = addclass(root, amountofclasses, adjustedbottomy)
                classlist.append(ist2)

            elif amountofclasses == 3:
                ist3 = addclass(root, amountofclasses, adjustedbottomy)
                classlist.append(ist3)

            elif amountofclasses == 4:
                ist4 = addclass(root, amountofclasses, adjustedbottomy)
                classlist.append(ist4)
                

class addclass:
  
    def __init__(self, root, instancenum, adjustedbottomy):
        self.instancenum = instancenum
        self.id = "Entry" + " " + str(amountofclasses)
        ft = tkFont.Font(family='Times',size=10)

        self.canvas = Canvas(root).place(x=533,y=adjustedbottomy,width=35,height=30)

        self.buttonvar = IntVar()
        self.buttonoutput = 0

        self.standardbutton = Radiobutton(self.canvas, indicatoron=0, text="S", variable= self.buttonvar, font='Dosis, 10', value=0, command = self.setvar(0)).place(x=533,y=adjustedbottomy,width=35,height=30)
        self.honorsbutton = Radiobutton(self.canvas, indicatoron=0, text="H", variable= self.buttonvar, font='Dosis, 10', value=1, command = self.setvar(1)).place(x=573,y=adjustedbottomy,width=35,height=30)
        self.apbutton = Radiobutton(self.canvas, indicatoron=0, text="AP", variable= self.buttonvar, font='Dosis, 10', value=2, command = self.setvar(2)).place(x=613,y=adjustedbottomy,width=35,height=30)

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
        entlst.append(AddClassNameEntry)
        entlst.append(AddGradeEntry)
    
    def setvar(self, n):
        self.buttonoutput = n




def AddButtoncalled():
    classmaker(root)

def GButton_374_command():
        global AddGradeEntry, AddClassNameEntry
        gradeDictionary.clear()
        NameandGradelist.clear()
        levellst.clear()


        for i in range(int(len(entlst))):
            if i % 2 > 0:
                pass
            else:
                Classname = str(entlst[i].get())
                Classgrade = entlst[i+1].get()
                NameandGradelist.append([Classname, Classgrade])
        
        for i in range(len(classlist)):
            levellst.append(classlist[i].buttonoutput)

        for i in range(len(levellst)):
            addGrade(NameandGradelist[i][0].upper(), NameandGradelist[i][1], levellst[i])
                
        
        print(gradeDictionary)
        print(GPACalculator(gradeDictionary, True))

def pritn():
     print("ahh")
if __name__ == "__main__":
    global root
    root = tk.Tk()
    app = App(root)
    classmaker(root)

    root.mainloop()
