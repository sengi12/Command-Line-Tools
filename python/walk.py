import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

name = "cmd.exe"
path = "C:\Program Files"

print "Searching for",name,"in",path,"...\n"
print "Output : ", find(name, path)