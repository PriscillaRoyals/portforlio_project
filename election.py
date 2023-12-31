# CREATED BY PRISCA EKHAGUERE AND MOHPHETH EKHAGUERE
# election polls system

import os

def display_heading():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nBLOCKCHAIN INSTITUTE OF TECHNOLOGY")
    print("WELCOME TO THE BCIT STUDENT PRESIDENT ELECTION")

def get_user_input():
    username = input("\nEnter your name: ")
    return username.strip()

def user_already_voted(username, voters_file='voters.txt'):
    with open(voters_file, 'r') as file:
        voters = file.readlines()
    return username + '\n' in voters

def candidate_already_added(candidate_name, candidates_file='candidates.txt'):
    with open(candidates_file, 'r') as file:
        candidates = [line.strip().lower() for line in file.readlines()]
    return candidate_name.strip().lower() in candidates

def record_voter(username, voters_file='voters.txt'):
    with open(voters_file, 'a') as file:
        file.write(username + '\n')

def display_candidates(candidates_file='candidates.txt'):
    with open(candidates_file, 'r') as file:
        candidates = file.readlines()
    for i, candidate in enumerate(candidates, 1):
        print(f"{i}. {candidate.strip()}")

def cast_vote(candidate_index, candidates_file='candidates.txt', number_file='number.txt'):
    with open(candidates_file, 'r') as file:
        candidates = file.readlines()
    
    if candidate_index < 1 or candidate_index > len(candidates):
        print("Invalid choice.")
        return False
    
    with open(number_file, 'r+') as file:
        votes = file.readlines()
        votes[candidate_index - 1] = str(int(votes[candidate_index - 1]) + 1) + '\n'
        file.seek(0)  # move to the beginning of the file
        file.writelines(votes)
        file.truncate()  # truncate the remaining file content after the new content
    return True

def display_results(candidates_file='candidates.txt', number_file='number.txt'):
    with open(candidates_file, 'r') as cfile:
        candidates = cfile.readlines()
    
    with open(number_file, 'r') as nfile:
        votes = nfile.readlines()
    
    print("\nElection Results:")
    print("Candidate".ljust(20), "Votes")
    print("-" * 30)
    for candidate, vote in zip(candidates, votes):
        print(candidate.strip().ljust(20), vote.strip())


def add_candidate(candidates_file='candidates.txt', number_file='number.txt'):
    new_candidate = input("Enter the name of the new candidate: ").strip()

    if candidate_already_added(new_candidate, candidates_file):
        print(f"Candidate {new_candidate} has already been added.")
        return

    with open(candidates_file, 'a') as cfile:
        cfile.write(new_candidate + '\n')

    with open(number_file, 'a') as nfile:
        nfile.write('0\n')

    print(f"Candidate {new_candidate} added successfully.")
def ensure_file_exists(filename, initial_content=''):
    """Ensure that a given file exists, or create it with optional initial content."""
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write(initial_content)

def setup_files():
    ensure_file_exists('voters.txt')
    ensure_file_exists('candidates.txt')
    ensure_file_exists('number.txt')

def main():
    while True:
        display_heading()
        print("\nMenu:")
        print("1. Vote")
        print("2. Add Candidate")
        print("3. View Results")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        if choice == 1:
            username = get_user_input()

            if user_already_voted(username):
                print("You have already voted.")
            else:
                display_candidates()
                try:
                    candidate_index = int(input("Enter the number of the candidate you want to vote for: "))
                    if cast_vote(candidate_index):
                        record_voter(username)
                        print("Thank you for voting!")
                except ValueError:
                    print("Invalid input. Please enter a valid candidate number.")
        elif choice == 2:
            add_candidate()
        elif choice == 3:
            display_results()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    setup_files()  # Ensure the necessary files exist or create them.
    main()
