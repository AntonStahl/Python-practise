user1 = raw_input("Enter Rock, Paper or Scissors:")
user2 = raw_input("Enter Rock, Paper or Scissors:")

if user1 == "Rock" and user2 == "Paper":
	print "Player 2 wins"

elif user1 == "Rock" and user2 == "Rock":
	print"No one wins"
	
elif user1 == "Rock" and user2 == "Scissors":
	print"Player 1 wins"
	
elif user1 == "Paper" and user2 == "Rock":
	print"Player 1 wins"
	
elif user1 == "Paper" and user2 == "Paper":
	print"No one wins"
	
elif user1 == "Paper" and user2 == "Scissors":
	print"Player 2 wins"
	
elif user1 == "Scissors" and user2 == "Paper":
	print"Player 1 wins"

elif user1 == "Scissors" and user2 == "Rock":
	print"Player 2 wins"

else:
	print "No one wins"