#Module: Using Dictionaries - Project "Scrabble"

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Question 1 Create a dictionary regrouping the two lists "letters" and "points", with elements of "letters" as keys and elements of "points" as values of the dictionary

letter_to_points = {letter:point for letter, point in zip(letters, points)}

print(letter_to_points)


#Question 2 Add a key:value pair to letter_to_points

letter_to_points[" "] = 0

print(letter_to_points)


#Question 3-4-5-6 Create a function to compute the score of any word 

def score_word(word):
  point_total = 0
  for letter in word:
    if letter in letter_to_points:
      point_total += letter_to_points[letter]
    else:
      point_total += 0
  return point_total

#example with word "LIFE"
print(score_word("LIFE"))


#Question 7-8

brownie_points = score_word("BROWNIE")
print(brownie_points)


#Question 9

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

print(player_to_words)


#Question 10
player_to_points = {}


#Question 11-12-13-14
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)


#Question 15 - BONUS
def play_word(player, word):
  for value in player_to_words.values():
    value.append(word)
  
play_word('player1', 'STUPID')

print(player_to_words)


## Bonus 2
for letter in letters:
  letters.append(letter.lower())

print(letters)


