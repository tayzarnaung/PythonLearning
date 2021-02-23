import random
import time

# The parameters we require to execute the game:
def init():
	global count, display, word, already_guessed, length

	words_to_guess = ["promise", "border", "image", "dog", "up", ]

	word = random.choice(words_to_guess)
	length = len(word)
	display = '_' * length
	count = 0
	already_guessed = []


# A loop to re-execute the game when the first round ends:
def play_loop():
	play_again = ""
	def askQ():
		nonlocal play_again
		play_again = input("Do You want to play again? y = yes, n = no \n")
	while play_again not in ["y", "n", "Y", "N"]:
		askQ()
	if play_again == "y" or play_again == "Y":
		init()
		hangman()
	elif play_again.lower() == "n":
		print("Thanks For Playing! We expect you back again!")
		exit()


def hangman():
	global count, display, word, already_guessed
	limit = 5
	print("Guess this Hangman Word: " + display)
	guess = input("Enter your guess: \t")
	guess = guess.strip()
	if len(guess) == 0 or len(guess) >= 2 or guess <= "9":
		print("Invalid Input, Try a letter")
		hangman()

	elif guess in word:
		already_guessed.extend([guess])
		# already_guessed.append(guess)
		index = word.find(guess)
		word = word[:index] + "_" + word[index + 1:]
		display = display[:index] + guess + display[index + 1:]

	elif guess in already_guessed:
		print("Try another letter.\n")

	else:
		count += 1

		if count < 5:
			time.sleep(1)
			print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

		elif count == 5:
			time.sleep(1)
			print("Wrong guess. You are hanged!!!\n")
			print("The word was:", already_guessed, word)
			play_loop()

	if word == '_' * length:
		print("Congrats! You have guessed the word correctly!")
		play_loop()

	elif count != limit:
		hangman()


init()
hangman()
