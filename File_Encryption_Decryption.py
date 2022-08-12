import pyAesCrypt,getpass,os
print("\nApp need to be in same folder where files are to be operated")
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
while(1):
	choice=input("\nenter 1 to encrypt, 2 to decrypt, 3 to exit: ")
	if choice =='1':
		# encrypt
		filename=input("enter file name with extension: ")
		while(1):
			print("*** password will not be visible ***")
			password1=getpass.getpass("enter password: ")
			password2=getpass.getpass("enter password again: ")
			if password1==password2:
				try:
					pyAesCrypt.encryptFile(filename, filename+".aes", password1, bufferSize)
					print(filename,"encrypted and saved with filename",filename+".aes in same folder")
					os.remove(filename)
				except IOError:
					print(filename,"not found in this folder")
				break
			else:
				print("both passwords not matched")
	elif choice=='2':
		# decrypt
		filename=input("enter file name with extension (without .aes): ")
		print("*** password will not be visible ***")
		password=getpass.getpass("enter password: ")
		try:
			pyAesCrypt.decryptFile(filename+".aes", filename, password, bufferSize)
			print(filename+".aes","decrypted and saved in same folder")
			os.remove(filename+".aes")
		except:
			print("some error occured")
	elif choice=='3':
		# exit
		break