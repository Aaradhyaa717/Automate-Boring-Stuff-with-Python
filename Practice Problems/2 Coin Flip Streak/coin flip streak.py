import random
numberOfStreaks = 0
coin_flip = []
streaks = 0

for experimentNumber in range(10000):

# Code that creates a list of 100 'heads' or 'tails' values.
  for flip in range(100):
    flip= random.randint(0,1)
    if flip == 1:
      coin_flip.append('H') # HEADS
    else:
      coin_flip.append('T') #TAILS

# Code that checks if there is a streak of 6 heads or tails in a row.
  
  for item in range(len(coin_flip)-1):
    #checking for similarity of adjacent items in the list
    if coin_flip[item] == coin_flip[item + 1]:
      streaks= streaks + 1
    else:
      streaks = 0
    
    if streaks == 6:
      numberOfStreaks = numberOfStreaks + 1    
  # re initializing coin flip
  coin_flip = []      

# 100 flips are made 10000 times
total_flips = 10000 * 100

# probablity of six streaks is given by number of streaks divided by total flips
chance_of_six_streak = numberOfStreaks / total_flips
print('Chance of streak: %s%%' % chance_of_six_streak)