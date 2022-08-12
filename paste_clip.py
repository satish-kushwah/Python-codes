
try:
	import pyautogui
except:
	print("\nPlease wait, we are installing 'pyautogui' library on your machine...\n")
	from pip._internal import main as pipmain
	pipmain(['install', 'pyautogui'])
	try:
		import pyautogui
	except:
		input("\n'pyautogui' library not installed. May be there is no internet connection, try again with active connection or manually install by running 'pip install pyautogui' command in Command Prompt.\nPress enter to exit and run script again.")
		quit()
try:
	import pyperclip
except:
	print("\nPlease wait, we are installing 'pyperclip' library on your machine...\n")
	from pip._internal import main as pipmain
	pipmain(['install', 'pyperclip'])
	try:
		import pyperclip
	except:
		input("\n'pyperclip' library not installed. May be there is no internet connection, try again with active connection or manually install by running 'pip install pyperclip' command in Command Prompt.\nPress enter to exit and run script again.")
		quit()
import pyautogui,pyperclip,time,random
input("press enter if you have copied the message to be send ")
n=int(input('how many times u want to send same message: '))
print('Set the cursor in message box within 20 seconds')
seconds=20;
while(seconds):
	print("starting sending message in",seconds,"seconds")
	seconds=seconds-1
	time.sleep(1)
print("sending mesages...")
for i in range(n):
	pyautogui.hotkey('ctrl','v')
	pyautogui.press('enter')	
print(n,"messages sent")