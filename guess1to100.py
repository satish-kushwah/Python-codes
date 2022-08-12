print("Please think of a number between one and one hundred.\nI'll guess your number.\nYou tell me if I'm  too high, too low, or correct.")
low=0
high=100
guess=50
count=1
while(1):
	print("\nI guess:",guess)
	choice=input("too (h)igh, too (l)ow, or (c)orrect?\n")
	if choice=='h':
		high=guess
		guess=guess-int((high-low)/2)		
		count=count+1
	elif choice=='l':
		low=guess
		guess=guess+int((high-low)/2)
		count=count+1
	elif choice=='c':
		print("I got it! it took",count," turns.")
		break
	else:
		print("Sorry, I didn't understand you...")