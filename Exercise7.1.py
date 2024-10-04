fh = open('exercise7_1datapage.txt')
#print(fh)

for line in fh:
    linescorrected = line.rstrip()
    print(linescorrected.upper())
