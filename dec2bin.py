n=int(input("enter a decimal number to convert it to binary : "))
binary="" #intially no values in binray string
while(n!=0): #calculating binary reverse
    rem=n%2
    n=n//2
    binary=binary+str(rem)
binary=binary[::-1] #reversing the string to get binary number
print("binary of given number is : ",binary) #printing binary number