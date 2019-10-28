import os

def run(**orgs):

    print "[*] in dirlister module"
    files = os.listdir(".")

    return str(files)
