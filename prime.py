import math
def isPrime(n):
	# for i in range(2,int(n/2)+1):   # simple version
	for i in range(2,int(math.sqrt(n))+1):
		if(n%i==0):
			return False
	# 1 is not prime
	if n==1:
		return False
	# if number do not have any factor
	return True

while(1):
	x=int(input("enter number to check if it is prime, 0 to exit: "))
	if x==0:
		break
	res=isPrime(x);
	if res:
		print("prime")
	else:
		print("not prime")
		