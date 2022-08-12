import random
while(1):
	random_num=random.randint(1,100)
	count=0
	while(1):
		x=int(input('guess the number between 1 and 100 or enter 0 to quit game: '))
		if x==0:
			print('game quited')
			play_again=input("enter 'yes' if u want to play again, or 'no' to stop game ")
			break
		elif x<1 or x>100:
			print('please guess number between 1 and 100 both inclusive')
			# count+=1
		elif x==random_num:
			count+=1
			print('Number correctly guessed ',random_num,' you got correcrt number in ',count,' attempts')
			play_again=input("enter 'yes' if u want to play again, or 'no' to stop game  ")
			break
		elif random_num>x:
			count+=1
			print('your guess is low')
		elif random_num<x:
			count+=1
			print('your guess is high')
	if play_again=='yes':
		continue
	else:
		break



