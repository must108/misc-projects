import difflib

with open('src/data/new.txt') as f1, open('src/data/sgb-words.txt') as f2: 
    var1 = (f1.read().splitlines())
    var2 = (f2.read().splitlines())

d = difflib.Differ()
diff = d.compare(var1, var2)

print("Starting merge...\n")
with open ('src/data/res.txt', 'w') as res:
    res.write('\n'.join(diff))
print("Done with merge!\n")

f1.close()
f2.close()
res.close()
