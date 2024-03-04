import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
guessed_letter = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letter:
      print(f"You have already guesed the letter {guess}")
    else:
      guessed_letter.append(guess)
    #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          #Test code:
          #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
          if letter == guess:
              display[position] = letter
  
      #Check if user is wrong.
      if guess not in chosen_word:
          lives -= 1
          print(f"{guess} is not in the word.")
          if lives == 0:
              end_of_game = True
              print("You lose.")
  
      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")
  
      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("You win.")


    print(stages[lives])