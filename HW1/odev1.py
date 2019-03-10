# Preprocess - check entry
def preProcess(num):
	if (w_number > 0)  and (w_number  < 9):
		return True
	else:
		return False
#End of preProcess

	
while True:
	box = 4 # pigeonhole : number of fruit kinds (banana , apple , orange , and strawberry)
	print("Please enter number of fruits withdrawals (Max : Number of fruits = 8 fruits : ")
	w_number = int(input())  # object , pigeon
	if preProcess(w_number) == True:
		if w_number <= box:
			print(" It is possible that all fruits may be distinct - no pigeonhole rule")
		else:
			if w_number == 8:
				print(" all pair matched")
			else:
				minimum = w_number % box
				print(" It is possible that " + str(minimum) + " pair matched")
			
	else:
		print("Range must be between 1 - 8 ")

