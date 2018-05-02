def display_message(period):
	num_ending = ""
	if period == 1:
		num_ending = "st"
	elif period == 2:
		num_ending = "nd"
	elif period == 3:
		num_ending = "rd"
	else:

		num_ending = "th"
	print ("good morning" + str(period) + num_ending + "period!")
	
