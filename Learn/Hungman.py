

import random
names = ["Cow", "Cat", "Dog", "Lion", "Goat"]


def play():
	game = raw_input ("Do you want to play the game again? y/n \n")
	if game == "n":
		print "Goodbye"
		return "n"
	else:
		game == "y"
		return "y"

def check_finished(choice, guessed_letters):
	for letter in choice:
		if letter not in guessed_letters:
			return False
	return True

def guess():	
	game = "y"
	while game == "y":
		guessed_letters = [] 
		choice = random.choice(names).lower()
		item = list ("_" * len(choice))
	#	name_guessed = []
		trials = 0
		while trials < 8:
			
			
			print "".join(item)
			print choice
			user_input = raw_input ("Guess the letters to form a word \n")
			while len(user_input)>1:
				 print "input a letter not a word"
			guessed_letters.append(user_input)
			print user_input

			for index in range(len(choice)):
				if choice[index] == user_input:
					item[index] = user_input
			if check_finished(choice, guessed_letters) == True:
				trials = 8
				print "You Win!" 

			trials += 1
		game = play()
guess()



		

  