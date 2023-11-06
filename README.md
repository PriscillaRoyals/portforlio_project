# Student-Election-System(Using Python language)

Voting system for candidates standing for College president.
It uses the concept of file handling.

## List of files:

1. candidates.txt = This file contains the number of candidates participating in elections.
2. `number.txt` = This contains no of votes for each candidate.
3. `voters.txt` = This contains the voters who have voted.
4. `election.py` = This file compute the winner of election by computing the votes for each candidates from the file `number.txt`.

## Rules followed:

1. You can vote only once.
2. Enter names as per registered in college.
3. You can add new candidates.
4. Student from any branch can participate.

### Overview:

This Python script:

- **Displays a menu** for users to vote, add a candidate, view results, or exit.
- **Handles user voting** by:
  - Checking if the user has already voted.
  - Allowing the user to vote if they haven’t voted before.
  - Recording the user's vote.
- **Allows for the addition of new candidates** to the election, updating the candidates' list and initializing the vote count for the new candidate.
- **Displays the election results**, showing the candidates and their respective vote counts.
- **Validates user input**, ensuring that the choices entered are numerical and within the valid range of options.
- Confirms that the required files exist or creates them if they don't. For the purpose of initialization, when the `candidates.txt` and `voters.txt` files are created, they can be left empty. However, the `number.txt` file should be initialized based on the number of candidates, which in this case would be zero if the file is just being created.
