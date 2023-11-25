import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog as fd 
from GPACalculatorBackEnd import *
import time as time

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
        global labelList, entryList, buttonList, weightedToggled, menubar
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

        filename = tk.PhotoImage(file = "backround.png")
        background_label = tk.Label(root, image=filename)
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
        CalculateButton["command"] = CalculateGPACalled
        CalculateButton["cursor"] = "hand2"


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
        AddButton["cursor"] = "hand2"

        # Create A Button
        settingsimg = tk.PhotoImage(file = "SettingsButton.png")
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

        self.canvas = tk.Canvas(root).place(x=533,y=adjustedbottomy,width=35,height=30)

        self.buttonvar = tk.IntVar()
        self.buttonoutput = 0

        self.standardbutton = tk.Radiobutton(self.canvas, indicatoron=0, text="S", variable= self.buttonvar, font='Dosis, 10', value=0, command = lambda n=0: self.setvar(n), cursor= "hand2").place(x=533,y=adjustedbottomy,width=35,height=30)
        self.honorsbutton = tk.Radiobutton(self.canvas, indicatoron=0, text="H", variable= self.buttonvar, font='Dosis, 10', value=1, command = lambda n=1: self.setvar(n), cursor= "hand2").place(x=573,y=adjustedbottomy,width=35,height=30)
        self.apbutton = tk.Radiobutton(self.canvas, indicatoron=0, text="AP", variable= self.buttonvar, font='Dosis, 10', value=2, command =lambda n=2: self.setvar(n), cursor= "hand2").place(x=613,y=adjustedbottomy,width=35,height=30)

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
                nameAndGradelist.append([className, classGrade])
        
        for i in range(len(classInstancelist)):
            levelList.append(classInstancelist[i].buttonoutput)
        
        for i in range(len(levelList)):
            addGrade(nameAndGradelist[i][0], nameAndGradelist[i][1].upper(), levelList[i])
                
        print(gradeDictionary)
        try:
            root.delete("TMP")
            Error = tk.Label(root, text = "GPA: " + str(GPACalculator(gradeDictionary, CalculateWeighted)), fg = "White", font = ("Dosis", 12), bg= "#010005", tags="TMP")
        
            
        except:
            Error = tk.Label(root, text = "GPA of 0 or an Error Has Occured", fg = "RED", font = ("Dosis", 12), bg= "#010005", tags="TMP")
            
        Error.pack(side=BOTTOM, pady= 45)

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
    .insert(0, "Hello, world!")
    print(name)

def saveFile():
    gradeDictionary.clear()
    nameAndGradelist.clear()
    levelList.clear()
    
    files = [('GPA Calculator Files', '*.gpa')] 
    file = fd.asksaveasfile(filetypes = files, defaultextension = files) 
    
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
    
    print(file)

if __name__ == "__main__":
    global root, menubar
    root = tk.Tk()
    app = App(root)
    classmaker(root)
    root.config(menu=menubar)
    root.mainloop()