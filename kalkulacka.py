import re

print("Tomkova kalkulacka")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
	global run
	global previous
	equation = input("Enter equation:")
	if equation == 'quit':
		run = False
	else:
		equation = re.sub('[a-zA-Z,.:()+" "]', "", equation)
		previous = eval(equation)		
		
		
		print("You typed", equation)

while run:
	performMath()


