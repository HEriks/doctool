import sys
# - f: Function description
# - p: Parameters
# - c: Complexity
print("Welcome, this tool will help you to quickly generate a short summary of your programs.")
fileName = input("Please enter the search path of your file (including file ending): ")
f = open(fileName, "r")
commentChars = input("Please enter the comment character(s) of your document: ")

line = 1
numFunc = 0
print("--- Functions ---")
for x in f:                                         # Check every line in the document
    x = x.strip()                                   # Removes whitespaces
    if len(x) > 1:
        if (x[:len(commentChars)] == commentChars): # Checks for comments using the specified comment character(s)
            if ('f:' in x):                         # Function description
                print("Line " + str(line) + ":")
                print(x[2:])
                numFunc = numFunc+1
                
            elif ('p:' in x):                       # Params
                print(x[2:])
            elif ('c:' in x):                       # Complexity
                print(x[2:])
            
    line = line + 1

print("--- Summary ---")                            # Print summary
print("Number of lines: " + str(line))
print("Number of documented functions: " + str(numFunc))
