rooms=int(input("Enter number of rooms: "))
price=float(input("Enter price per sq foot: "))
print() #printing blank  line
total_footage=0 # taking initial total footage to 0
for i in range(rooms):
	length=int(input("Enter room "+str(i+1)+" length: "))
	width=int(input("Enter room "+str(i+1)+" width: "))
	footage=length*width #footage of room
	total_footage=total_footage+footage # adding footage of room to total footage
total_cost=price*total_footage
print('\n\n') #printing 2 blank lines
print("Price per sq foot: $"+str(price))
print("Total sq feet: "+str(total_footage))
print("House total cost: $"+str(f"{total_cost:,.2f}"))  #printing total cost in required format
import os # importing os for using pause
os.system("pause") #waiting for user to press any key