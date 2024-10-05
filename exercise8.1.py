filehandle = open('exercise7_1datapage.txt')

for line in filehandle:
    line = line.rstrip()
    words = line.split()
    if len(words)<5:
        continue
    if words[0] != 'From':
        continue
    print(words[2])