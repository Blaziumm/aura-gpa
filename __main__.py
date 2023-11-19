import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from GPACalculatorBackEnd import *


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

        #Account_Frame
        newRowFrame = tk.Frame(root, width=500, height=1000)
        newRowFrame.pack(side="bottom", pady=12)

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
        CalculateButton["relief"] = "raised"
        AddButton.place(x=415,y=463,width=125,height=25)
        AddButton["command"] = AddButtoncalled
        
        AddClassLabel=tk.Label(root)
        AddClassLabel["font"] = ft
        AddClassLabel["fg"] = "#140a1f"
        AddClassLabel["justify"] = "center"
        AddClassLabel["text"] = "Name of Class"
        AddClassLabel.place(x=200-xshift,y=90,width=130,height=30)

        AddGradeLabel=tk.Label(root)
        AddGradeLabel["font"] = ft
        AddGradeLabel["fg"] = "#140a1f"
        AddGradeLabel["justify"] = "center"
        AddGradeLabel["text"] = "Grade"
        AddGradeLabel.place(x=360-xshift,y=90,width=130,height=30)

        # Create A Button
        on_button=tk.Button(root)
        on_button["anchor"] = "center"
        on_button["justify"] = "center"
        on_button["relief"] = "raised"
        on_button.place(x=20,y=455,width=25,height=25)
        on_button["command"] = pritn

def addlabel(root):
        global amountofclasses, AddGradeEntry, AddClassNameEntry, xshift, butlst
        adjustedbottomy = 0
        adjustedtopy = 0
        adjustedbottomy = 130 + amountofclasses * 40
        adjustedtopy = 90 + adjustedtopy * 40
        id = "Entry" + " " + str(amountofclasses)
        ft = tkFont.Font(family='Times',size=10)


        amountofclasses = amountofclasses + 1
        AddClassNameEntry=tk.Entry(root)
        AddClassNameEntry["borderwidth"] = "1px"
        AddClassNameEntry["font"] = ft
        AddClassNameEntry["fg"] = "#140a1f"
        AddClassNameEntry["justify"] = "center"
        AddClassNameEntry["text"] = "Class" + id
        AddClassNameEntry.place(x=200-xshift,y=adjustedbottomy,width=130,height=30)

        AddGradeEntry=tk.Entry(root)
        AddGradeEntry["borderwidth"] = "1px"
        AddGradeEntry["font"] = ft
        AddGradeEntry["fg"] = "#140a1f"
        AddGradeEntry["justify"] = "center"
        AddGradeEntry["text"] = "Grade" + id
        AddGradeEntry.place(x=360-xshift,y=adjustedbottomy,width=130,height=30)

        AddStandardButton=tk.Radiobutton(root)
        AddStandardButton["anchor"] = "center"
        AddStandardButton["justify"] = "center"
        AddStandardButton.place(x=510-xshift,y=adjustedbottomy,width=35,height=35)
        AddStandardButton["command"] = pritn

        AddHonorsButton=tk.Radiobutton(root)
        AddHonorsButton["anchor"] = "center"
        AddHonorsButton["justify"] = "center"
        AddHonorsButton.place(x=550-xshift,y=adjustedbottomy,width=35,height=35)
        AddHonorsButton["command"] = pritn

        AddAPButton=tk.Radiobutton(root)
        AddAPButton["anchor"] = "center"
        AddAPButton["justify"] = "center"
        AddAPButton.place(x=590-xshift,y=adjustedbottomy,width=35,height=35)
        AddAPButton["command"] = pritn
        
        butlst.append(AddStandardButton)
        butlst.append(AddHonorsButton)
        butlst.append(AddAPButton)
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
