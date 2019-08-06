import sys
print("Welcome, this tool will help you to quickly generate a short summary of your programs")
userInput = input("Please enter the search path of your file (including file ending)")
f = open(userInput, "r")
line = 1
numFunc = 0
print("--- Functions ---")
for x in f:
    x = x.strip()
    if len(x) > 1:
        # print(x[:2])
        if (x[:2] == "//"):
            if ('f:' in x):
                print("Line " + str(line) + ":")
                print(x[2:])
                numFunc = numFunc+1
            elif ('p:' in x):
                print(x[2:])
            elif ('c:' in x):
                print(x[2:])
            
        line = line + 1

print("--- Summary ---")
print("Number of lines: " + str(line))
print("Number of documented functions: " + str(numFunc))
