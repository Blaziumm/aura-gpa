import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from GPACalculatorBackEnd import *

levellst = [0,0,0,0,0,0,0,0]
amountofclasses = 0
xshift = 70

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
        


def addlabel(root):
        global amountofclasses, AddGradeEntry, AddClassNameEntry, xshift, butlst
        v=0
        adjustedbottomy = 0
        adjustedbottomy = 90 + amountofclasses * 40
        id = "Entry" + " " + str(amountofclasses)
        ft = tkFont.Font(family='Times',size=10)

        if amountofclasses == 8:
            maxclasses = Label(root, text = "Maximum Amount Of Classes Added", fg = "red", font = ("Helvetica", 12))
            maxclasses.place(x=245,y=430)
            amountofclasses == 404
        elif amountofclasses == 404:
             pass
        else:
            amountofclasses = amountofclasses + 1
            

            AddClassNameEntry=tk.Entry(root)
            AddClassNameEntry["borderwidth"] = "1px"
            AddClassNameEntry["font"] = ft
            AddClassNameEntry["fg"] = "#140a1f"
            AddClassNameEntry["justify"] = "center"
            AddClassNameEntry["text"] = "Class" + id
            AddClassNameEntry.place(x=185,y=adjustedbottomy,width=130,height=30)

            AddGradeEntry=tk.Entry(root)
            AddGradeEntry["borderwidth"] = "1px"
            AddGradeEntry["font"] = ft
            AddGradeEntry["fg"] = "#140a1f"
            AddGradeEntry["justify"] = "center"
            AddGradeEntry["text"] = "Grade" + id
            AddGradeEntry.place(x=355,y=adjustedbottomy,width=130,height=30)


            butlst.append(Radiobutton(root, indicatoron=0, text="S", variable=levellst[amountofclasses], font='Verdana, 10', value=0).place(x=533,y=adjustedbottomy,width=35,height=30))
            butlst.append(Radiobutton(root, indicatoron=0, text="H", variable=levellst[amountofclasses], font='Dosis, 10', value=1).place(x=573,y=adjustedbottomy,width=35,height=30))
            butlst.append(Radiobutton(root, indicatoron=0, text="AP", variable=levellst[amountofclasses], font='Verdana, 10', value=2).place(x=613,y=adjustedbottomy,width=35,height=30))
            entlst.append(AddClassNameEntry)
            entlst.append(AddGradeEntry)
def AddButtoncalled():
    
    addlabel(root)      
def GButton_374_command():
        global AddGradeEntry, AddClassNameEntry
        gradeDictionary.clear()

        for i in range(int(len(entlst))):
            if i % 2 > 0:
                pass
            else:
                Classname = str(entlst[i].get())
                Classgrade = entlst[i+1].get()
                if not Classname == "" and not Classgrade == "":
                    addGrade(Classname.upper(), Classgrade, 0)
        
        print(gradeDictionary)
        print(GPACalculator(gradeDictionary, True))
def pritn():
     print("ahh")
if __name__ == "__main__":
    global root
    root = tk.Tk()
    app = App(root)
    addlabel(root)

    root.mainloop()
