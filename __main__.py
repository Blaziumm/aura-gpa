import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from GPACalculatorBackEnd import *

amountofclasses = 0

class App:
    def __init__(self, root):
        
        global GradeEntry, ClassNameEntry, lbllst, newRowFrame, entlst
        lbllst = []
        entlst = []
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

        bg = PhotoImage(file = "clickable-buttons-ui.png") 
        # Show image using label 
        label1 = Label(root, image = bg) 
        label1.place(x = 0, y = 0)  

        #Account_Frame
        newRowFrame = tk.Frame(root, width=500, height=1000, bg='#140a1f')
        newRowFrame.pack(side="bottom", pady=12)

        CalculateButton=tk.Button(root)
        CalculateButton["anchor"] = "center"
        CalculateButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        CalculateButton["font"] = ft
        CalculateButton["fg"] = "#000000"
        CalculateButton["justify"] = "center"
        CalculateButton["text"] = "Calculate"
        CalculateButton["relief"] = "raised"
        CalculateButton.place(x=245,y=463,width=125,height=25)
        CalculateButton["command"] = GButton_374_command

        AddButton=tk.Button(root)
        AddButton["anchor"] = "center"
        AddButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        AddButton["font"] = ft
        AddButton["fg"] = "#000000"
        AddButton["justify"] = "center"
        AddButton["text"] = "Add Class"
        CalculateButton["relief"] = "raised"
        AddButton.place(x=415,y=463,width=125,height=25)
        AddButton["command"] = AddButtoncalled
        
        
    
def addlabel(root):
        global amountofclasses, AddGradeEntry, AddClassNameEntry
        adjustedbottomy = 0
        adjustedtopy = 0
        adjustedbottomy = 130 + amountofclasses * 40
        adjustedtopy = 90 + adjustedtopy * 40
        id = "Entry" + " " + str(amountofclasses)

        amountofclasses = amountofclasses + 1
        AddClassNameEntry=tk.Entry(root)
        AddClassNameEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        AddClassNameEntry["font"] = ft
        AddClassNameEntry["fg"] = "#140a1f"
        AddClassNameEntry["justify"] = "center"
        AddClassNameEntry["text"] = "Class" + id
        AddClassNameEntry.place(x=200,y=adjustedbottomy,width=130,height=30)

        AddClassLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        AddClassLabel["font"] = ft
        AddClassLabel["fg"] = "#140a1f"
        AddClassLabel["justify"] = "center"
        AddClassLabel["text"] = "Name of Class"
        AddClassLabel.place(x=200,y=adjustedtopy,width=130,height=30)

        AddGradeLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        AddGradeLabel["font"] = ft
        AddGradeLabel["fg"] = "#140a1f"
        AddGradeLabel["justify"] = "center"
        AddGradeLabel["text"] = "Grade"
        AddGradeLabel.place(x=360,y=adjustedtopy,width=130,height=30)

        AddGradeEntry=tk.Entry(root)
        AddGradeEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        AddGradeEntry["font"] = ft
        AddGradeEntry["fg"] = "#140a1f"
        AddGradeEntry["justify"] = "center"
        AddGradeEntry["text"] = "Grade" + id
        AddGradeEntry.place(x=360,y=adjustedbottomy,width=130,height=30)
        entlst.append(AddClassNameEntry)
        entlst.append(AddGradeEntry)
        lbllst.append(AddClassLabel)
        lbllst.append(AddGradeLabel)
        
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
                addGrade(Classname.upper(), Classgrade, 0)
        
        print(gradeDictionary)
        print(GPACalculator(gradeDictionary, True))



if __name__ == "__main__":
    global root
    root = tk.Tk()
    app = App(root)
    addlabel(root)

    root.mainloop()
