def main():
	player_choice = Input("Rock Paper or Scissor")
	computer_choice = FUNCTION generate_random
	SWITCHCASE(player_choice)
		CASE rock
			IF computer_choice == rock
				DISPLAY Draw
			ELSEIF computer_choice == paper
				DISPLAY Lose
			ELSE
				DISPLAY Win
			EXIT

		CASE paper
			IF computer_choice == rock
				DISPLAY Win
			ELSEIF computer_choice == paper
				DISPLAY Draw
			ELSE
				DISPLAY Lose
			EXIT

		CASE scissors
			IF computer_choice == rock
				DISPLAY Lose
			ELSEIF computer_choice == paper
				DISPLAY Win
			ELSE
				DISPLAY Draw
			EXIT

END rps_logic