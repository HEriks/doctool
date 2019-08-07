import sys
import os
# Explanation of keycharacters:
# - f: Function name
# - d: Function description
# - p: Parameters
# - c: Complexity
# - o: Output
    
# f: docu
# d: Summarises the selected document
# c: O(n)
# o: a list with the number of lines and number of documented functions
def docu():
    line = 1
    numFunc = 0
    ccl3 = ccl+3
    print("--- Functions ---")
    for x in f:                                         # Check every line in the document
        x = x.strip()                                   # Removes whitespaces
        if len(x) > 1:
            if (x[:ccl] == commentChars):               # Checks for comments using the specified comment character(s)
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
# e: Only runs when user has selected to get a file output from the program
def docuFile():
    nfD = open(sn,"w+")
    line = 1
    numFunc = 0
    ccl3 = ccl+3
    nfD.write("--- Functions ---")
    for x in f:                                         # Check every line in the document
        x = x.strip()                                   # Removes whitespaces
        if len(x) > 1:
            if (x[:ccl] == commentChars):               # Checks for comments using the specified comment character(s)
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


if __name__ == '__main__': 
    print("Welcome, this tool will help you to quickly generate a short summary of your programs.")

    fileName = input("Please enter the search path of your file (including file ending): ")
    f = open(fileName, "r")
    
    commentChars = input("Please enter the comment character(s) of your document: ")
    ccl = len(commentChars)     # The number of comment characters

    newFile = input("Do you want to create a document file? (y/n): ")
    if ((newFile == 'y') | (newFile == 'Y')):
        sn = fileName + "_summary.txt"
        s = sn.rsplit(".", 1)
        num = 1
        while os.path.exists(sn):
            sn = s[0] + "(" + str(num) + ")." + s[1]
            num = num + 1

        infoF = docuFile()
        summariseFile(infoF)
    else:
        info = docu()               # Document the code
        summarise(info)             # Summarise the document


### For testing ###
# f: nothingFunc ***TEST***
# d: Function that does nothing
# p: None
#c: O(1)