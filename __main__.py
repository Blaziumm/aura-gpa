import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog as fd 
from GPACalculatorBackEnd import *
import time as time
import json

levelList = []
classInstancelist = []
ErrorList = []
nameAndGradelist = []

adjustedbottomy = 0
amountofclasses = 0
xshift = 70

settingsWindowOpen = False
CalculateWeighted = True
class App:
    def __init__(self, root):
        global labelList, entryList, buttonList, weightedToggled, menubar, ft
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

        weightedToggled = tk.IntVar()

        filename = tk.PhotoImage(file = "images/backround.png")
        background_label = tk.Label(root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = filename

        try:
            ft = tkFont.Font(family='Dosis',size=10)
        except:
            ft = tkFont.Font(family='Times',size=10)

        CalculateButton=tk.Button(root, anchor = "center",bg = "#ffffff",font= ft,fg= "#010005",justify= "center",text= "Calculate",
                                  relief= "raised",cursor= "hand2", command= CalculateGPACalled).place(x=245,y=463,width=125,height=25)

        AddButton=tk.Button(root,cursor= "hand2", command = AddButtoncalled, relief= "raised", text= "Add Class", justify = "center", fg= "#000000", font= ft, 
                            bg = "#f0f0f0", anchor= "center").place(x=415,y=463,width=125,height=25)

        # Create A Button
        settingsimg = tk.PhotoImage(file = "images/SettingsButton.png")
        settings=tk.Button(root, image = settingsimg, border = 0)
        settings["anchor"] = "center"
        settings["justify"] = "center"
        settings["relief"] = "raised"
        settings["bg"] = "#010005"
        settings["fg"] = "#010005"
        settings["image"] = settingsimg
        settings.place(x=20,y=455,width=30, height=30)
        settings["command"] = settingButtonClicked
        settings["cursor"] = "hand2"
        settings.image = settingsimg

        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=openFile)
        filemenu.add_command(label="Save", command=saveFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

def classmaker(root):
        global amountofclasses, AddGradeEntry, AddClassNameEntry, xshift, buttonList

        amountofclasses = amountofclasses + 1

        if amountofclasses == 9:
            Error = tk.Label(root, text = "Maximum Amount Of Classes Added (8)", fg = "red", font = ("Dosis", 12))
            Error.place(x=245,y=430)
            amountofclasses == 10
            
        elif amountofclasses == 10:
             pass
        
        else:
            adjustedbottomy = 50 + amountofclasses * 40
            if amountofclasses == 1:
                instanceOne = addclass(root, amountofclasses, adjustedbottomy)
                classInstancelist.append(instanceOne)
                ClassNameEntry1 = tk.Entry(root, borderwidth = "1px", font = ft, fg = "#140a1f",justify = "center").place(x=185,y=adjustedbottomy,width=130,height=30)
                GradeEntry1 = tk.Entry(root, borderwidth = "1px", font = ft, fg = "#140a1f",justify = "center").place(x=355,y=adjustedbottomy,width=130,height=30)
                entryList.append(ClassNameEntry1)
                entryList.append(GradeEntry1)

            elif amountofclasses == 2:
                instanceTwo = addclass(root, amountofclasses, adjustedbottomy)
                classInstancelist.append(instanceTwo)
                ClassNameEntry2 = tk.Entry(root, borderwidth = "1px", font = ft, fg = "#140a1f",justify = "center").place(x=185,y=adjustedbottomy,width=130,height=30)
                GradeEntry2 = tk.Entry(root, borderwidth = "1px", font = ft, fg = "#140a1f",justify = "center").place(x=355,y=adjustedbottomy,width=130,height=30)
                entryList.append(ClassNameEntry2)
                entryList.append(GradeEntry2)

            elif amountofclasses == 3:
                instanceThree = addclass(root, amountofclasses, adjustedbottomy)
                classInstancelist.append(instanceThree)
                ClassNameEntry3 = tk.Entry(root, borderwidth = "1px", font = ft, fg = "#140a1f",justify = "center").place(x=185,y=adjustedbottomy,width=130,height=30)
                GradeEntry3 = tk.Entry(root, borderwidth = "1px", font = ft, fg = "#140a1f",justify = "center").place(x=355,y=adjustedbottomy,width=130,height=30)
                entryList.append(ClassNameEntry3)
                entryList.append(GradeEntry3)

            elif amountofclasses == 4:
                instanceFour = addclass(root, amountofclasses, adjustedbottomy)
                classInstancelist.append(instanceFour)
                ClassNameEntry4 = tk.Entry(root, borderwidth = "1px", font = ft, fg = "#140a1f",justify = "center").place(x=185,y=adjustedbottomy,width=130,height=30)
                GradeEntry4 = tk.Entry(root, borderwidth = "1px", font = ft, fg = "#140a1f",justify = "center").place(x=355,y=adjustedbottomy,width=130,height=30)
                entryList.append(ClassNameEntry4)
                entryList.append(GradeEntry4)

            elif amountofclasses == 5:
                instanceFive = addclass(root, amountofclasses, adjustedbottomy)
                classInstancelist.append(instanceFive)
                ClassNameEntry5 = tk.Entry(root, borderwidth = "1px", font = ft, fg = "#140a1f",justify = "center").place(x=185,y=adjustedbottomy,width=130,height=30)
                GradeEntry5 = tk.Entry(root, borderwidth = "1px", font = ft, fg = "#140a1f",justify = "center").place(x=355,y=adjustedbottomy,width=130,height=30)
                entryList.append(ClassNameEntry5)
                entryList.append(GradeEntry5)

            elif amountofclasses == 6:
                instanceSix = addclass(root, amountofclasses, adjustedbottomy)
                classInstancelist.append(instanceSix)
                ClassNameEntry6 = tk.Entry(root, borderwidth = "1px", font = ft, fg = "#140a1f",justify = "center").place(x=185,y=adjustedbottomy,width=130,height=30)
                GradeEntry6 = tk.Entry(root, borderwidth = "1px", font = ft, fg = "#140a1f",justify = "center").place(x=355,y=adjustedbottomy,width=130,height=30)
                entryList.append(ClassNameEntry6)
                entryList.append(GradeEntry6)

            elif amountofclasses == 7:
                instanceSeven = addclass(root, amountofclasses, adjustedbottomy)
                classInstancelist.append(instanceSeven)
                ClassNameEntry7 = tk.Entry(root, borderwidth = "1px", font = ft, fg = "#140a1f",justify = "center").place(x=185,y=adjustedbottomy,width=130,height=30)
                GradeEntry7 = tk.Entry(root, borderwidth = "1px", font = ft, fg = "#140a1f",justify = "center").place(x=355,y=adjustedbottomy,width=130,height=30)
                entryList.append(ClassNameEntry7)
                entryList.append(GradeEntry7)

            elif amountofclasses == 8:
                instanceEight = addclass(root, amountofclasses, adjustedbottomy)
                classInstancelist.append(instanceEight)
                ClassNameEntry8 = tk.Entry(root, borderwidth = "1px", font = ft, fg = "#140a1f",justify = "center").place(x=185,y=adjustedbottomy,width=130,height=30)
                GradeEntry8 = tk.Entry(root, borderwidth = "1px", font = ft, fg = "#140a1f",justify = "center").place(x=355,y=adjustedbottomy,width=130,height=30)
                entryList.append(ClassNameEntry8)
                entryList.append(GradeEntry8)


class addclass:
    def __init__(self, root, instancenum, adjustedbottomy):
        global entryList
        self.instancenum = instancenum
        self.id = "Entry" + " " + str(amountofclasses)

        self.canvas = tk.Canvas(root).place(x=533,y=adjustedbottomy,width=35,height=30)

        self.buttonvar = tk.IntVar()
        self.buttonoutput = 0

        self.standardButton = tk.Radiobutton(self.canvas, indicatoron=0, text="S", variable= self.buttonvar, font='Dosis, 10', value=0, command = lambda n=0: self.setvar(n), cursor= "hand2").place(x=533,y=adjustedbottomy,width=35,height=30)
        self.honorsButton = tk.Radiobutton(self.canvas, indicatoron=0, text="H", variable= self.buttonvar, font='Dosis, 10', value=1, command = lambda n=1: self.setvar(n), cursor= "hand2").place(x=573,y=adjustedbottomy,width=35,height=30)
        self.apButton = tk.Radiobutton(self.canvas, indicatoron=0, text="AP", variable= self.buttonvar, font='Dosis, 10', value=2, command =lambda n=2: self.setvar(n), cursor= "hand2").place(x=613,y=adjustedbottomy,width=35,height=30)
    
    def setvar(self, n):
        self.buttonoutput = n

def AddButtoncalled():
    classmaker(root)

def CalculateGPACalled():
        global AddGradeEntry, AddClassNameEntry, CalculateWeighted
        gradeDictionary.clear()
        nameAndGradelist.clear()
        levelList.clear()
        for i in range(int(len(entryList))):
            if i % 2 > 0:
                pass
            else:
                className = str(entryList[i].get())
                classGrade = entryList[i+1].get()
        for i in range(len(classInstancelist)):
            levelList.append(classInstancelist[i].buttonoutput)
        for i in range(len(levelList)):
            addGrade(nameAndGradelist[i][0], nameAndGradelist[i][1].upper(), levelList[i])
                
        print(gradeDictionary)
        try:
            root.delete(Error)
            if GPACalculator(gradeDictionary, CalculateWeighted) == 101:
                Error = tk.Label(root, text = "No Classes have been inputed", fg = "RED", font = ("Dosis", 12), bg= "#010005")
            elif GPACalculator(gradeDictionary, CalculateWeighted) == 202:
                Error = tk.Label(root, text = "An Error Has Occured, please input all data", fg = "RED", font = ("Dosis", 12), bg= "#010005")
            else:
                Error = tk.Label(root, text = "GPA: " + str(GPACalculator(gradeDictionary, CalculateWeighted)), fg = "White", font = ("Dosis", 12), bg= "#010005")

            
        except:
            Error = tk.Label(root, text = "Error Has Occured, please input all data.", fg = "RED", font = ("Dosis", 12), bg= "#010005")
            
        Error.pack(side="bottom", pady= 45)

def settingButtonClicked():
    global settingsWindowOpen, weightedToggled, CalculateWeighted
    settingsWindowOpen = reverseBool(settingsWindowOpen)
     # Create the popup window
    settings = tk.Toplevel()
    # Set the title of the popup window
    settings.title("Settings")
    # Set the size of the popup window
    settings.geometry("400x200")
    
    # Add a label to the popup window
    label = tk.Label(settings, text="This is a popup window.")
    label.pack(side="top")
    Weighted = tk.Radiobutton(settings, indicatoron=1, text="Calculate Weighted", variable= weightedToggled, font='Dosis, 10', value=1, command=lambda b=True: requestToChangeWeighted(b), cursor= "hand2").pack()
    UnWeighted = tk.Radiobutton(settings, indicatoron=1, text="Calculate Unweighted", variable= weightedToggled, font='Dosis, 10', value=2, command=lambda b=False: requestToChangeWeighted(b), cursor= "hand2").pack()

    # Show the Settings window
    settings.mainloop()

def requestToChangeWeighted(b):
    global CalculateWeighted
    if b:
        CalculateWeighted = True
    else:
        CalculateWeighted = False

def reverseBool(bool):
    if bool:
        return(False)
    else:
        return(True)

def donothing():
    pass

def openFile():
    name= fd.askopenfilename() 
    
    with open(name, 'r') as f:
        list_from_file = json.load(f)

    print(list_from_file)

def saveFile():
    gradeDictionary.clear()
    nameAndGradelist.clear()
    levelList.clear()
    
    files = [('GPA Calculator Files', '*.gpa')] 
    file = fd.asksaveasfile(filetypes = files, defaultextension = files) 
    if not file == "": 
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



        with open(file, 'w') as f:
            json.dump(list_to_store, f)
    
    print(file)


if __name__ == "__main__":
    global root, menubar
    root = tk.Tk()
    app = App(root)
    classmaker(root)
    root.config(menu=menubar)
    root.mainloop()