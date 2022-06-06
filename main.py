from art import logo,vs
from random import randint
from game_data import data
from replit import clear
#print(logo)
current_list=[]
current_list.append(data[randint(0,len(data)-1)])
continued=True
score=0 
while(continued==True):
  print(logo)
  A=current_list[0]
  x=data[randint(0,len(data)-1)]
  if x==A:
    x=data[randint(0,len(data)-1)]
  current_list.append(x)
  #print(f"Current List: {current_list}")
  B=current_list[1]
  print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}")
  print(vs)
  print(f"Against B: {B['name']}, a {B['description']} from {B['country']}")
  print(f"Current score: {score}.")
  choice=(input("Who has more followers? Type 'A' or 'B': ")).capitalize()
  if choice=='A':
    if A['follower_count']>B['follower_count']:
      score+=1
      current_list.pop(0)
    else:
      continued=False
  elif choice=='B':
    if B['follower_count']>A['follower_count']:
      score+=1
      current_list.pop(0)
    else:
      continued=False
  else:
    print("Invalid")
    continued=False
  clear()
print(f"Sorry, that's wrong. Final score: {score}")    