# yes, it includes the is_divisible function
# yes, implement an is_power function that takes two arguments
# yes,  is_power function call is_divisible
# yes, is_power function call itself recursively
# yes, is_power function include code for the base case of the two arguments being equal
# yes, is_power function include code for the base case of the second argument being "1"
# yes, submission include correct output for the five test cases

def is_divisible(x,y):
	if x%y==0:
		return True
	else:
		return False

def is_power(a,b):
	if a!=1 and b==1:
		return False
	elif(is_divisible(a,b)==False):
		return False
	elif a==b:
		return True
	else:
		return is_power(a/b,b)

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))