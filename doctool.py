import sys
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *

# Explanation of keycharacters:
# - f: Function name
# - d: Function description
# - p: Parameters
# - c: Complexity
# - o: Output

# GUI

#Create the window and GUI elements
wd = Tk()
wd.title("doctool")
wd.geometry('360x80')

lb1 = Label(wd, text="Please select which file you want to document", anchor="nw")
lb1.grid(column = 0, row = 0, sticky = W)

# f: browse
# d: Lets the user select the desired file
def browse():
    global fn       # Create global file name variable 
    fn = filedialog.askopenfilename()
    txt.focus()

btn = Button(wd, text = "Browse", command = browse)
btn.grid(column = 1, row = 0, sticky = W)

lb2 = Label(wd, text="Enter the comment character(s) of your document: ")
lb2.grid(column = 0, row = 2, sticky = W)
txt = Entry(wd, width=3)
txt.grid(column=1, row=2, sticky = W)

# f: letsgo
# d: Runs the program with the GUI
def letsgo():
    commentChars = txt.get()
    global sn
    sn = fn + "_summary.txt"
    s = sn.rsplit(".", 1)
    num = 1
    while os.path.exists(sn):
        sn = s[0] + "(" + str(num) + ")." + s[1]
        num = num + 1
    info = docuFile(fn, commentChars, sn)
    summariseFile(info)

    messagebox.showinfo("Info", "Output file created in same folder as source file.")

btnGo = Button(wd, text = "Go", command = letsgo)
btnGo.grid(column=0, row=6, sticky = W)

# f: docuFile
# d: Like "docu()" but writes to a file instead
# p: filename, comment character(s), name of new file 
# e: Only runs when user has selected to get a file output from the program
def docuFile(fileName, cc, sn):
    f = open(fileName, "r")
    nfD = open(sn,"w+")
    ccl = len(cc)
    ccl3 = ccl+3
    line = 1
    numFunc = 0
    
    nfD.write("--- Functions ---")
    for x in f:                                         # Check every line in the document
        x = x.strip()                                   # Removes whitespaces
        if len(x) > 1:
            if (x[:ccl] == cc):                         # Checks for comments using the specified comment character(s)
                if ('f:' in x[:(ccl3)]):                # Function description
                    nfD.write("\nLine " + str(line) + ":" + x[(ccl3):] + "\n")
                    numFunc = numFunc+1
                elif ('d:' in x[:(ccl3)]):             # Description of the function
                    nfD.write("Despcription:" + x[(ccl3):] + "\n")
                elif ('p:' in x[:(ccl3)]):             # Params
                    nfD.write("Parameters: " + x[(ccl3):] + "\n")
                elif ('c:' in x[:(ccl3)]):             # Complexity
                    nfD.write("Complexity: " + x[(ccl3):] + "\n")
                elif ('o:' in x[:(ccl3)]):             # Output
                    nfD.write("Output: " + x[(ccl3):] + "\n")
                elif ('e:' in x[:(ccl3)]):             # Extra info
                    nfD.write("Extra info: " + x[(ccl3):] + "\n")
                
        line = line + 1
    nfD.close
    return [line, numFunc]

# f: summariseFile
# d: like "summarise" but instead appends results to a file
# e: only runs when user has selected to get a file output
def summariseFile(info):
    nfS = open(sn,"a")
    nfS.write("\n--- Summary ---\n")                            # Write summary to file
    nfS.write("Number of lines: " + str(info[0]) + "\n")
    nfS.write("Number of documented functions: " + str(info[1]) + "\n")
    nfS.close

wd.mainloop()