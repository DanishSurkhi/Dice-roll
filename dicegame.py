import random
def roll():
    max=6
    min=1
    roll=random.randint(min,max)
    return roll

while True:
    players=input("choose number of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            print("good value")
            break
        else:
            print("bad value")
    else:
         print("format invalid") 
max_score =50
# list comprehension uses input to write number of players 
player_score=[0 for i in range(players)]
# print(scores)

while max(player_score)<max_score:
    for player in range(players):
        
        current_score=0
        while True:
            should_roll=input(f"does player: {player} you wanna roll the dice(y/n)")
            if should_roll.lower()!="y":
                break
            value=roll()
            if value ==1:
                print(f"you rolled a {value}")
                print("turn over score is now zero")
                current_score=0
                break
            else:
                current_score +=value
                print(f"the player rolls a {value}")
            print(f"the player current score: {current_score}")
        
        player_score[player]+=current_score
        print(f"score of player {player} is {player_score[player]}")

max_score=max(player_score)
winner=player_score.index(max_score)
print(f"the winner is {winner}")    


 







