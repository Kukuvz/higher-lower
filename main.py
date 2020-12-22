import random
from art import logo, vs
from game_data import data
from replit import clear

def format_data(account):
  """Format account data to print"""
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and returns if they got it right"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"  

#Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

#Make game repeatable
while game_should_continue:

  #Generate random account

  #Making account at B become next account position A
  account_a = account_b
  account_b = random.choice(data)

  if account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Compare B: {format_data(account_b)}")

  #Ask user
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()


  #Check if user is correct
  ##Get follower count of each account
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  #clear screen
  clear()
  print(logo)

  #Give user feedback
  #Score keeping
  if is_correct:
    score += 1
    print(f"You`re right! Current score: {score}")
  else:
    game_should_continue = False
    print(f"Sorry, that`s wrong. Final score: {score}")  




