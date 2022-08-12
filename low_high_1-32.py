import random
games=0
while(1):
	games=games+1
	random_num=random.randint(1,32)
	attempts=0
	print("I am thinking of a number from 1-32 inclusive. Try to guess it.")
	while(1):
		x=int(input('What is your guess? '))
		if x<1 or x>32:
			print('Try again. Must be 1-32.')
		elif x==random_num:
			attempts+=1
			play_again=input("Congrats, you guessed it in "+str(attempts)+" tries. If you want to play again, enter yes. Anything else to quit. ") 
			break
		elif random_num>x:
			attempts+=1
			print('Your guess is too low')
		elif random_num<x:
			attempts+=1
			print('Your guess is too high')
	if play_again=='yes':
		continue
	else:
		print("You played "+str(games)+" games.")
		break