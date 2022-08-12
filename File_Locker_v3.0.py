def getListOfFiles(dirName):
    # create a list of file and sub directories 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)            
    return allFiles

import getpass,os
try:
    import pyAesCrypt
except:
    print('PyAesCrypt library is being installed on your system, make sure you are connected to internet...\n')
    from pip._internal import main as pipmain
    pipmain(['install', 'pyAesCrypt'])
    try:
        import pyAesCrypt
    except:
        input("pyAesCrypt library not installed, run 'pip install pyAesCrypt' command in Command Prompt, press enter to exit and run script again after installation")
        quit()
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
print("(You need to press enter key after typing your input)\n")
print("Current folder - ",os.getcwd())
choice0=input("\nEnter\n1 to Lock/Unlock single file\n2 to Lock/Unlock multiple files\n3 to exit program\n: ")
if(choice0=='1'):
    while(1):
        choice1=input("\nEnter\n1 to Lock file\n2 to Unlock file\n3 to exit program\n: ")
        if choice1 =='1':
            # encrypt
            filename=input("Enter file name with extension: ")
            if filename.split('.')[-1] not in ["exe","aes"]:
                input("Please REMEBER your password. if you forget it, file will get locked permanently.\nPress Enter to continue ")
                while(1):
                    print("*** Password will not be visible ***")
                    password1=getpass.getpass("Enter password: ")
                    password2=getpass.getpass("Enter password again: ")
                    if password1==password2 and password1!="":
                        try:
                            print("Locking file, please wait...")
                            pyAesCrypt.encryptFile(filename, filename+".aes", password1, bufferSize)
                            print(filename,"locked and saved with filename",filename+".aes in same folder")
                            os.remove(filename)
                        except:
                            print("\n",filename,"not locked")
                        break
                    else:
                        print("\nBoth passwords not matched")
            else:
                print(filename,"not alloweed to lock")
        elif choice1=='2':
            # decrypt
            filename=input("Enter file name with extension (without .aes): ")
            print("*** Password will not be visible ***")
            password=getpass.getpass("Enter password: ")
            try:
                print("Unlocking file, please wait...")
                pyAesCrypt.decryptFile(filename+".aes", filename, password, bufferSize)
                print(filename+".aes","unlocked and saved in same folder")
                os.remove(filename+".aes")
            except:
                print("Wrong password / Some error occured")
        else:
            # exit
            break
elif(choice0=='2'):
    choice1=input("\nEnter\n1 to Lock/Unlock files only of this folder\n2 to Lock/Unlock files including sub-folders\n3 to exit program\n: ")
    if choice1=='1':
        print("Locking/Unlocking files only of this folder")
        from os import listdir
        from os.path import isfile, join
        mypath=os.getcwd()
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        try:
            onlyfiles.remove(__file__.split('\\')[-1])
        except:
            print("",end="")
    elif choice1=='2':
        print("Locking/Unlocking files of this folder and sub-folders")
        onlyfiles=getListOfFiles(os.getcwd())
        try:
            onlyfiles.remove(__file__)
        except:
            print("",end="")
    else:
        quit()
    choice1=input("\nEnter\n1 to Lock files\n2 to Unlock files\n3 to exit program\n: ")
    if choice1 =='1':
        # encrypt
        print("----- Locking -----")
        input("Please REMEBER your password. if you forget it, files will get locked permanently.\nPress Enter to continue ")
        while(1):
            print("*** Password will not be visible ***")
            password1=getpass.getpass("Enter password: ")
            password2=getpass.getpass("Enter password again: ")
            if password1==password2 and password1!="":
                print("Locking files, please wait...")
                for i in range(len(onlyfiles)):
                    try:
                        if(onlyfiles[i].split('.')[-1] not in ["exe","aes"]):
                            pyAesCrypt.encryptFile(onlyfiles[i], onlyfiles[i]+".aes", password1, bufferSize)
                            os.remove(onlyfiles[i])
                            print(onlyfiles[i],"locked successfully")
                    except:
                        print("\n",onlyfiles[i],"--- NOT LOCKED\n")
                break
            else:
                print("\nBoth passwords not matched")
    elif choice1=='2':
        # decrypt
        print("----- Unlocking -----")
        print("*** Password will not be visible ***")
        password=getpass.getpass("Enter password: ")
        try:
            print("Unlocking files, please wait...")
            for i in range(len(onlyfiles)):
                try:
                    pyAesCrypt.decryptFile(onlyfiles[i], onlyfiles[i][0:-4], password, bufferSize)
                    os.remove(onlyfiles[i])
                    print(onlyfiles[i],"unlocked successfully")
                except:
                    print("\n",onlyfiles[i],"--- NOT UNLOCKED (may be wrong password)\n")
        except:
            print("Wrong password / Some error occured")
    else:
        quit()
    input("\nPress Enter to exit")

