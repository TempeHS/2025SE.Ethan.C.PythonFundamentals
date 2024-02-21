def main():
	player_choice = input("Rock Paper or Scissor")
	computer_choice = FUNCTION generate_random
	match player_choice:
		case "rock":
			match computer_choice:
				case "rock":
					print("Draw")
				case "paper":
					print("Lose")
				case "scissors":
					print("Win")

		case "paper":
			match computer_choice:
				case "rock":
					print("Win")
				case "paper":
					print("Draw")
				case "scissors":
					print("Lose")

		case "scissors":
			match computer_choice:
				case "rock":
					print("Lose")
				case "paper":
					print("Win")
				case "scissors":
					print("Draw")

main()