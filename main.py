from art import logo , vs
from game_data import data
from replit import clear
import random
print(logo)
score= 0
game_should_continue = True
account_b =random.choice(data)  #account b has to account a when the answer is right


def format_data(account):
  """format the account data into printable format"""
  account_name = account["name"]
  account_desc =account["description"]
  account_country = account["country"]
  return f"{account_name} a {account_desc} from {account_country}"

def check_answer(guess, a_follower, b_follower):
  """ use if ur answer is right or wrong"""
  if a_follower > b_follower:
    if guess == "a":
      return guess
    else:
      return guess == "b"


while game_should_continue:
  account_a = account_b # so account a = b
  account_b =random.choice(data) #and account b is a random data again
  while account_a ==  account_b:
    account_b = random.choice(data)

  print(f"compare A :{format_data(account_a)}")
  print(vs)
  print(f"compare B : {format_data(account_b)}")


  guess = input("Who has more followers? Tyoe A or B : ").lower()

  a_follower = account_a["follower_count"]
  b_follower = account_b["follower_count"]
  is_correct =check_answer(guess , a_follower , b_follower)

  clear()
  print(logo)

  if is_correct:
    score += 1
    print(f"You got it , your current score is {score}")
  else:
    game_should_continue = False
    print(f"You are wrong, your score is {score}")