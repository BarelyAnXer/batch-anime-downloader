from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Treeview

#import fouranime

def browse():
    dir_path = filedialog.askdirectory(initialdir="/", title="Select Location")
    pathEnt.delete(0, END)
    pathEnt.insert(0, dir_path)
    return


def functemp():
    print(var1.get())

root = Tk()
root.configure(background="blue")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 770
height = 500
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
root.resizable(False, False)

# toolbar

toolbar = Frame(root, width=770, height=40)
toolbar.configure(background="green")
toolbar.place(x=0, y=0)

bbb = Button(toolbar, text="temp",command=functemp)
bbb.place(x=0,y=0)
# toolbar

# gen details
genDetails = Frame(root, width=770, height=110)
genDetails.configure(background="yellow")
genDetails.place(x=0, y=40)

lbl1 = Label(genDetails, text="General Details")
lbl1.place(x=10, y=10)

lbl2 = Label(genDetails, text="Anime URL")
lbl2.place(x=10, y=40)

urlEnt = Entry(genDetails, width=50)
urlEnt.place(x=100, y=40)

# b1 = Button(genDetails, text="Search Urls")
# b1.place(x=420, y=50)

lbl3 = Label(genDetails, text="Save To:")
lbl3.place(x=10, y=70)

pathEnt = Entry(genDetails, width=50)
pathEnt.place(x=100, y=70)

browseBtn = Button(genDetails, text="Browse", command=lambda: browse())
browseBtn.place(x=420, y=67)

# gen Details

# episdoe details
epiDetails = Frame(root, width=770, height=350)  # 120
epiDetails.configure(background="purple")
epiDetails.place(x=0, y=150)

lbl4 = Label(epiDetails, text="Episdoe Details")
lbl4.place(x=10, y=10)

lbl4 = Label(epiDetails, text="Configure Episodes")
lbl4.place(x=10, y=50)

configEnt = Entry(epiDetails, width=25)
configEnt.place(x=140, y=50)

var1 = IntVar(value=1)
allChkBox = Checkbutton(epiDetails,variable=var1)
allChkBox.place(x=300, y=50)

tv = Treeview(epiDetails, column=("fn", "sz", "pr", "tr"), show="headings")
tv.heading("fn", text="File Name")
tv.column("fn", width=250, stretch=YES)

tv.heading("sz", text="Size")
tv.column("sz", width=125, stretch=NO)

tv.heading("pr", text="Progress")
tv.column("pr", width=125, stretch=NO)

tv.heading("tr", text="Transfer Rate")
tv.column("tr", width=125, stretch=YES)

tv.insert("", "end", values=("Nekopara Ep1", "253.23MB", "Completed", "mabilis"))

tv.place(x=10, y=100)

# verscrlbar = Scrollbar(epiDetails, orient="vertical", command=tv.yview)


# episdode details

root.mainloop()
