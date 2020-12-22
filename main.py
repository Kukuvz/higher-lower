import random
from replit import clear
from art import logo
from art import vs
from game_data import data

SCORE = 0

def print_a_b(dict_a, dict_b):
  name_a = dict_a["name"]
  follow_a = dict_a["follower_count"]
  description_a = dict_a["description"]
  country_a = dict_a["country"]
  print(f"Compare A: {name_a}, a {description_a}, from {country_a}")
  print(f"Pssst, followers = {follow_a}")
  name_b = dict_b["name"]
  follow_b = dict_b["follower_count"]
  description_b = dict_b["description"]
  country_b = dict_b["country"]
  print(vs)
  print(f"Against B: {name_b}, a {description_b}, from {country_b}")
  print(f"Pssst, followers = {follow_b}")

def compare(member_a, member_b):
  follow_a = member_a["follower_count"]
  follow_b = member_b["follower_count"]
  if follow_a > follow_b:
    return member_a
  elif follow_a < follow_b:
    return member_b   
def game():
  print(logo)
  member_a = random.choice(data)
  should_continue = False

  while should_continue == False:
    member_b = random.choice(data)
    print_a_b(member_a, member_b)

    choice = (input("Who has more followers? Type 'A' or 'B'")).lower()
    ab_choice = {}
    if choice == "a":
      ab_choice = member_a
    else:
      ab_choice = member_b 

    winner = compare(member_a, member_b)
   
    if ab_choice == winner:
      global SCORE
      SCORE+=1
      member_a = winner
      clear()
      game()
    elif ab_choice != winner:
      should_continue == True
      clear()
      print(f"You Lose. Your score: {SCORE}")
  # clear()
  # print(logo)
  # print(f"You Lose. Your score: {SCORE}")
  
        

game()