f_opn = open("file.txt", "r")
for line in f_opn:
    if "hello" in line:
        print line
f_opn.close()
