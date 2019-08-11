import sys
import os
from tkinter import *
from tkinter import filedialog
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
wd.geometry('450x100')

# f: pupres
# d: Makes a popup window with the result (if you choose to not print the output)

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

lb2 = Label(wd, text="Enter the comment character(s) of your document")
lb2.grid(column = 0, row = 2, sticky = W)
txt = Entry(wd, width=3)
txt.grid(column=1, row=2, sticky = W)


lb3 = Label(wd, text="Do you want to create a txt file with the documentation?")
lb3.grid(column = 0, row = 4, sticky = W)

# Radio buttons for selecting whether to print the result or create and output file
selected = BooleanVar()
rad1 = Radiobutton(wd, text = "Yes", value = True, variable = selected)
rad2 = Radiobutton(wd, text = "No", value = False, variable = selected)
rad1.grid(column=1, row = 4, sticky = W)
rad2.grid(column=2, row = 4, sticky = W)

# f: letsgo
# d: Runs the program with the GUI
def letsgo():
    sct = selected.get()
    commentChars = txt.get()
    if not sct:
        info = docu(fn, commentChars)
        summarise(info)
    else:
        global sn
        sn = fn + "_summary.txt"
        s = sn.rsplit(".", 1)
        num = 1
        while os.path.exists(sn):
            sn = s[0] + "(" + str(num) + ")." + s[1]
            num = num + 1
        info = docuFile(fn, commentChars, sn)
        summariseFile(info)


btnGo = Button(wd, text = "Go", command = letsgo)
btnGo.grid(column=0, row=6, sticky = W)

# f: docu
# d: Summarises the selected document
# p: filename, comment character(s) 
# c: O(n)
# o: a list with the number of lines and number of documented functions
def docu(fileName, cc):
    f = open(fileName, "r")
    ccl = len(cc)
    ccl3 = ccl+3
    line = 1
    numFunc = 0
    
    print("--- Functions ---")
    for x in f:                                         # Check every line in the document
        x = x.strip()                                   # Removes whitespaces
        if len(x) > 1:
            if (x[:ccl] == cc):                         # Checks for comments using the specified comment character(s)
                if ('f:' in x[:(ccl3)]):                # Function description
                    print("\nLine " + str(line) + ":" + x[(ccl3):])
                    numFunc = numFunc+1
                elif ('d:' in x[:(ccl3)]):             # Description of the function
                    print("Despcription:" + x[(ccl3):])
                elif ('p:' in x[:(ccl3)]):             # Params
                    print("Parameters: " + x[(ccl3):])
                elif ('c:' in x[:(ccl3)]):             # Complexity
                    print("Complexity: " + x[(ccl3):])
                elif ('o:' in x[:(ccl3)]):             # Output
                    print("Output: " + x[(ccl3):])
                elif ('e:' in x[:(ccl3)]):             # Extra info
                    print("Extra info: " + x[(ccl3):])
                
        line = line + 1
    return [line, numFunc]

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

# f: summarise
# d: Summarises the document in a very basic way. Has to be run _after_ "docu()"
# p: info - a list with the info gathered from "docu()"
# c: O(1)
# o: None
# e: Can't be run alone in order to keep the complexity down (Counting number of lines is O(n) and is already done once)
def summarise(info):
    print("\n--- Summary ---")                            # Print summary
    print("Number of lines: " + str(info[0]))
    print("Number of documented functions: " + str(info[1]))

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