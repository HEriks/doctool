import sys
# - f: Function description
# - p: Parameters
# - c: Complexity
print("Welcome, this tool will help you to quickly generate a short summary of your programs.")
fileName = input("Please enter the search path of your file (including file ending): ")
f = open(fileName, "r")
commentChars = input("Please enter the comment character(s) of your document: ")
ccl = len(commentChars)                             # The number of comment characters
ccl2 = ccl + 2
ccl3 = ccl + 3
line = 1
numFunc = 0

print("--- Functions ---")
for x in f:                                         # Check every line in the document
    x = x.strip()                                   # Removes whitespaces
    if len(x) > 1:
        if (x[:ccl] == commentChars):               # Checks for comments using the specified comment character(s)
            if ('f:' in x[:(ccl3)]):                # Function description
                print("Line " + str(line) + ":" + x[(ccl3):])
                numFunc = numFunc+1
            elif ('d:' in x[:(ccl3)]):             # Description of the function
                print("Despcription:" + x[(ccl3):])
            elif ('p:' in x[:(ccl3)]):             # Params
                print("Parameters: " + x[(ccl3):])
            elif ('c:' in x[:(ccl3)]):             # Complexity
                print("Complexity: " + x[(ccl3):])
            elif ('o:' in x[:(ccl3)]):             # Output
                print("Complexity: " + x[(ccl3):])
            
            
    line = line + 1

print("--- Summary ---")                            # Print summary
print("Number of lines: " + str(line))
print("Number of documented functions: " + str(numFunc))

# For testing
# f: nothingFunc
# d: Function that does nothing
# p: None
#c: O(1)