#read all lines from file into list  
with open("text.txt","r") as f:
    lines = f.readlines()
    print(lines)
    
#total number of lines and print 2nd and 4th line
print(f"Total number of lines: {len(lines)}")
print(f"2nd line: {lines[1]}")
print(f"4th line: {lines[3]}")
    