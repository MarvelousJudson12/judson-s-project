>>> def monkey_trouble(tom_smiling, bob_smiling):
		if tom_smiling and bob_smiling:
			return True
		elif not bob_smiling and not tom_smiling:
			return True
		else:
			return False




>>>monkey_trouble(True, True)
True
>>>monkey_trouble(False, False)
False
>>>monkey_trouble(True, False)
False
>>>monkey_trouble(1,1)
True
>>>monkey_trouble(0,0)
True
>>>monkey_trouble(none,none)
True
>>>monkey_trouble("","")
False
>>>monkey_trouble("banana","banana")
True
