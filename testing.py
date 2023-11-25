import tkinter as tk

def callback():
    name= fd.askopenfilename() 
    print(name)
    
errmsg = 'Error!'
tk.Button(text='Click to Open File', 
       command=callback).pack(fill=tk.X)
tk.mainloop()