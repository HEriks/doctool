import sys
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
    # ccl2 = ccl+2
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

# f: summarise
# d: Summarises the document in a very basic way. Has to be run _after_ "docu()"
# p: info - a list with the info gathered from "docu()"
# c: O(1)
# o: None
# e: Can't be run alone in order to keep the complexity down (Counting number of lines is O(n) and is already done once)
def summarise(info):
    print("--- Summary ---")                            # Print summary
    print("Number of lines: " + str(info[0]))
    print("Number of documented functions: " + str(info[1]))

if __name__ == '__main__': 
    print("Welcome, this tool will help you to quickly generate a short summary of your programs.")

    fileName = input("Please enter the search path of your file (including file ending): ")
    f = open(fileName, "r")
    
    commentChars = input("Please enter the comment character(s) of your document: ")
    ccl = len(commentChars)     # The number of comment characters

    info = docu()               # Document the code
    summarise(info)             # Summarise the document


### For testing ###
# f: nothingFunc
# d: Function that does nothing
# p: None
#c: O(1)