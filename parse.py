with open("data/emails.txt", "r") as fp:
    file = fp.read()
    
arr = file.split()
print(len(arr))