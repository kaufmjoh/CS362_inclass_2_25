def fibonacci(a):

	#define base cases
	if a==1:
		return 0
	if a==2:
		return 1

	#define recursive call
	return (fibonacci(a-1) + fibonacci(a-2))

def factorial(a):
	
	if a==0:
		return 1
	if a==1:
		return 1

	return (a*factorial(a-1))
